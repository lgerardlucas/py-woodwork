const HomePage = {};

HomePage.init = function() {
    HomePage.binds();
}

HomePage.binds = function() {
    document.querySelectorAll('.product-image').forEach((element) => {
        element.addEventListener('click', HomePage.openImageModal);
    });

    document.querySelector('.modal-image').addEventListener('click', HomePage.closeImageModal);
}

HomePage.openImageModal = function(event) {
    const { target } = event;
    const modal = document.querySelector('.modal-image');

    modal.style.display = 'block';
    modal.querySelector('img').setAttribute('src', target.getAttribute('src'));
}

HomePage.closeImageModal = function() {
    const modal = document.querySelector('.modal-image');
    modal.style.display = 'none';
}

window.onload = HomePage.init;