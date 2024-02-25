"""
uptpy - Python FTP uploader with minumum overhead and zero extra dependencies.

I'd like a webspace updated as quickly & reliable as possible! How to do that?
We need to know what needs to be updated instead of just pushing all without
checking. For that we'll download a manifest file containing the files for each
target directory. If such file is not yet present the remote dirs are initially
scanned. Then we loop over a local manifest and sync anything off.
Afterwards we update the remote manifest.

Pros:
 * checks are done super quickly
 * actual update uploads are as compact as possible
 * deletions are handled as well (Of files once uploaded via uptpy)
 * any other remote dirs and files are ignored by default

Cons:
 * initially ALL files need to be uploaded (we "could" instead download first
   and update if necessary. TBD)
 * If a file is removed remotely uptpy wouldn't notice. (We could do a post-
   check to fix any missing files. TBD)
 * we need to have this remote manifest file (which could potentially be found
   on the server and reveal files and hashes) (we could however obfuscate it at
   least a little.)

"""
import os
import sys
import json
import time
import ftplib
import hashlib
import logging
import posixpath

logging.basicConfig()
log = logging.getLogger('uptpy')
log.setLevel(logging.DEBUG)

__version__ = '1.1.0'
__version_info__ = (1, 1, 0)
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
REMOTE_MANIFEST = '_GSVKSBKJBDU.json'
IGNORE_DOT_NAMES = True
ENCODING = 'utf8'
# ENCODING = 'latin-1'
# ENCODING = 'cp437'

# If this is set True uptpy will perform an initial remote scan! Anything that's
# not also in the local path will then be deleted!! Use only if you want to
# match local and remote 1 to 1! Otherwise uptpy will ONLY care about the local
# path files and ignore anything that's also on the server.
SCAN_REMOTE = False
MSG_DELE = '250 DELE command successful'
ERROR_UNICODE_REASON = 'invalid continuation byte'


def update(host='', user='', passwd='', local_path='', remote_path='', in_ftp=None):
    # type: (str, str, str, str, str, ftplib.FTP | None) -> int
    """Perform
    Log into FTP, check remote against given local path, resolve diffs.

    * dir missing remotely: create dir, upload all files
    * dir missing locally: remove containing files, delete dir
    * file missing remotely: upload
    * file missing locally: delete remotely
    * file different locally: upload
    """
    start_time = time.time()
    ftp, _ftp_created = get_ftp(host, user, passwd, ENCODING, in_ftp)

    remote_dirs = load_manifest(ftp, remote_path)
    if not remote_dirs:
        if SCAN_REMOTE:
            remote_dirs = scan_remote(ftp, remote_path)
        else:
            remote_dirs = {'': {}}

    local_dirs = scan_local(local_path)
    if remote_dirs == local_dirs:
        log.info(
            'No difference! All good! (check took %.3fs)' % (time.time() - start_time)
        )
        return 0

    num_changes = 0
    for rel_dir, dir_data in local_dirs.items():
        # dir missing remotely
        if rel_dir not in remote_dirs:
            mkdirs(ftp, remote_path, rel_dir)
            remote_dirs[rel_dir] = {}

        for file_name, ldata in dir_data.items():
            rel_path = posixpath.join(rel_dir, file_name)
            if file_name in remote_dirs[rel_dir]:
                rdata = remote_dirs[rel_dir][file_name]
                # all good if file exists and is identical
                if rdata.get('hash') == ldata['hash']:
                    continue
                log.info('File different! %s', rel_path)

            # upload if missing or changed
            _upload(ftp, rel_path, local_path, remote_path)
            num_changes += 1
            continue

        # delete files no longer local
        for file_name in set(remote_dirs[rel_dir]).difference(dir_data):
            try:
                result = ftp.delete(posixpath.join(remote_path, rel_dir, file_name))
                if result == MSG_DELE:
                    log.info('DELE: %s', posixpath.join(rel_dir, file_name))
                    num_changes += 1
            except ftplib.error_perm:
                pass

    # dir needs to be deleted
    for dir_name in sorted(set(remote_dirs).difference(local_dirs), reverse=True):
        # Might be directory with no files but subdirs that should be up!
        if any(ld.startswith(dir_name) for ld in local_dirs):
            continue

        for file_name in remote_dirs[dir_name]:
            try:
                result = ftp.delete(posixpath.join(remote_path, dir_name, file_name))
                if result == '250 DELE command successful':
                    log.info('DELE: %s', posixpath.join(dir_name, file_name))
                    num_changes += 1
            except ftplib.error_perm:
                pass

        dir_path = posixpath.join(remote_path, dir_name)
        try:
            res = ftp.rmd(dir_path)
            if res == '250 RMD command successful':
                log.info('RMD: %s', dir_path)
        except ftplib.error_perm as error:
            log.error('Error deleting "%s"!\n%s', dir_path, error)

    update_manifest(ftp, local_dirs, local_path, remote_path)

    if _ftp_created:
        ftp.close()

    return num_changes


def update_manifest(ftp, data, local_path, remote_path):
    """Update the remote manifest."""
    if not local_path:
        local_path = THIS_DIR
    tmp_local_mani = os.path.join(local_path, REMOTE_MANIFEST)
    with open(tmp_local_mani, 'w') as file_obj:
        json.dump(data, file_obj, sort_keys=True)
    _upload(ftp, REMOTE_MANIFEST, local_path, remote_path)


def _upload(ftp, rel_path, local_path, remote_path):
    # type: (ftplib.FTP, str, str, str) -> bool
    local_file_path = os.path.join(local_path, rel_path)
    rel_path = rel_path.replace(os.path.sep, posixpath.sep)
    with open(local_file_path, 'rb') as file_obj:
        try:
            res = ftp.storbinary(
                'STOR %s' % posixpath.join(remote_path, rel_path), file_obj
            )
            if res == '226 Transfer complete':
                log.info('STOR: %s', rel_path)
                return True
            log.error(res)
        except ftplib.error_perm:
            log.exception('Error uploading file "%s"', rel_path)
            log.info(
                'local file: %s exists:%s',
                local_file_path,
                os.path.isfile(local_file_path),
            )
            parent_dir = posixpath.dirname(posixpath.join(remote_path, rel_path))
            log.info('parent dir: %s exists:%s', parent_dir, os.path.isdir(parent_dir))

        return False


def scan_remote(ftp, remote_path, ignores=None):
    # type: (ftplib.FTP, str, list[str] | None) -> dict[str, dict[str, dict[str, str|int]]]
    log.info('Scanning remote path: %s ...', remote_path)
    data = {}
    t0 = time.time()
    _scan_remote(ftp, remote_path, '', data, ignores)
    print('%s took %.3fs' % ('_scan_remote', time.time() - t0))
    return data


def _scan_remote(ftp, root, path, data, ignores):
    # type: (ftplib.FTP, str, str, dict[str, dict[str, str]], list[str] | None) -> None
    files = {}
    try:
        for name, item in ftp.mlsd(posixpath.join(root, path)):
            if IGNORE_DOT_NAMES and name.startswith('.') or _is_ignored(name, ignores):
                continue
            if item['type'] == 'file':
                files[name] = {'size': int(item['size'])}
            elif item['type'] == 'dir':
                _scan_remote(ftp, root, posixpath.join(path, name), data, ignores)
    except UnicodeDecodeError as error:
        if error.reason == ERROR_UNICODE_REASON and ftp.encoding.lower() in (
            'utf8',
            'utf-8',
        ):
            raise Exception(
                'Try with a different encoding like `latin-1` or `cp437`!'
            ) from error
        raise error

    # Collect remote dirs no matter if files or not
    # to be able to delete empty folders.
    data[path] = files
    log.info('dir: %s - %i files', path, len(files))


def scan_local(root, ignores=None):
    # type: (str, list[str] | None) -> dict[str, dict[str, dict[str, str | int]]]
    data = {}
    _scan_local(root, '', data, ignores)
    return data


def _scan_local(root, path, data, ignores):
    # type: (str, str, dict[str, dict[str, dict[str, str | int]]], list[str] | None) -> None
    has_files, has_dirs = False, False
    _path = path.replace(os.path.sep, posixpath.sep)
    for item in os.scandir(os.path.join(root, path)):
        # for dirpath, _, filenames in os.walk(os.path.join(root, path)):
        if IGNORE_DOT_NAMES and item.name.startswith('.'):
            continue

        rel_path = os.path.join(path, item.name)
        if _is_ignored(rel_path, ignores):
            continue

        if item.is_file():
            data.setdefault(_path, {})[item.name] = {
                'size': os.path.getsize(item.path),
                'hash': _hsh(item.path),
            }
            has_files = True
        elif item.is_dir():
            _scan_local(root, rel_path, data, ignores)
            has_dirs = True

    # Collect directory when if has only subdirs but no files.
    if not has_files and has_dirs:
        data.setdefault(_path, {})


def _is_ignored(name, ignores):
    # type: (str, list[str] | None) -> bool
    """
    Check name or relative path against provided ignores.
    """
    if name == REMOTE_MANIFEST:
        return True

    if ignores is None:
        return False

    return False


def get_ftp(host, user, passwd, encoding=ENCODING, in_ftp=None):
    # type: (str, str, str, str, ftplib.FTP | None) -> tuple[ftplib.FTP, bool]
    if in_ftp is not None:
        return in_ftp, False

    log.info('Connecting to "%s" ...', host)
    try:
        ftp = ftplib.FTP(host, encoding=encoding)
    except Exception as error:
        raise Exception('Error creating connection to "%s"\n%s' % (host, error))

    result = ftp.login(user, passwd)
    log.info(result)
    log.info(ftp.getwelcome())
    return ftp, True


def _hsh(local_path):
    # type: (str) -> str
    hasherobj = hashlib.sha256()
    size = pow(2, 16)
    with open(local_path, 'rb') as fobj:
        buf = fobj.read(size)
        len_buf = len(buf)
        while len_buf > 0:
            hasherobj.update(buf)
            buf = fobj.read(size)
            len_buf = len(buf)
    return hasherobj.hexdigest()


def load_manifest(ftp, remote_path):
    # type: (ftplib.FTP, str) -> dict[str, dict[str, dict[str, str | int]]]
    try:
        content = read_remote(ftp, posixpath.join(remote_path, REMOTE_MANIFEST))
    except ftplib.error_perm:
        return {}

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return {}

    return data


def read_remote(ftp, path):
    # type: (ftplib.FTP, str) -> str
    lines = []
    ftp.retrlines('RETR ' + path, lines.append)
    return '\n'.join(lines)


def mkdirs(ftp, root, path=''):
    # type: (ftplib.FTP, str, str) -> None
    if path:
        path = path.replace(os.path.sep, posixpath.sep)
        path = posixpath.join(root, path)
    else:
        path = root

    parts = path.split(posixpath.sep)
    created = ''
    for i in range(1, len(parts) + 1):
        this_dir = posixpath.join(*parts[:i])

        # try and skip error 550. It's not utterly specific:
        #  "Requested action not taken. File unavailable (e.g., file not found, no access)."
        #  see: https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes
        # but it can't be that the parent dir isn't there (we're looping the path) and
        # without listing we cannot easily check for presence, It's also quicker than listing!
        try:
            ftp.mkd(this_dir)
        except ftplib.error_perm as error:
            if error.args[0].startswith('550'):
                continue
            raise error

        created = posixpath.join(*parts[:i])

    if created:
        log.info('MKD: %s', created)


if __name__ == '__main__':
    import sys

    if sys.argv[1:]:
        update(*sys.argv[1:6])
