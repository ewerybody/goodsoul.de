function navbar_toggle() {
    var nb_btn_icon = document.getElementsByClassName("nb_btn_icon")[0];
    nb_btn_icon.classList.toggle("nb_btn_icon_x");
    var nb_list = document.getElementsByClassName("nb_list")[0];
    nb_list.classList.toggle("nb_list_x");
}

function _connect_nb_btn() {
    const nb_btn = document.getElementsByClassName("nb_btn")[0];
    nb_btn.addEventListener('click', event => {
        navbar_toggle();
    });
}

window.onload=_connect_nb_btn;