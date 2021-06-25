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

/*---------Filter images in products ----------*/
filterSelection("all")

function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("filterDiv");
    if (c == "all") c = "";
    for (i = 0; i < x.length; i++) {
        w3RemoveClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
    }
}

function w3AddClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) { element.className += " " + arr2[i]; }
    }
}

function w3RemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnfurniture");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}