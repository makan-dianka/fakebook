function myFunction(x) {
    if (x.matches) {
        var mediaQ = document.querySelector('.media-q');
        mediaQ.classList.remove('form-box');
    } else {
        console.log("no match media query ");
    }
  }


var x = window.matchMedia("(max-width: 860px)")
myFunction(x)
x.addListener(myFunction)