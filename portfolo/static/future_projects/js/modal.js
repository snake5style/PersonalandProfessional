var modals = document.getElementsByClassName('modal');
// Get the button that opens the modal
var btns = document.getElementsByClassName("myBtn");
var spans=document.getElementsByClassName("close");
for(let i=0;i<btns.length;i++){
   btns[i].onclick = function() {
      modals[i].style.display = "block";
   }
}
for(let i=0;i<spans.length;i++){
    spans[i].onclick = function() {
        modals[i].style.display = "none";
    }
}


function myFunction(x) {
  if (x.matches) { // If media query matches
    document.body.style.backgroundColor = "#F5DEB3";
  } else {
   document.body.style.backgroundColor = "#FFDAB9;";
  }
}

var x = window.matchMedia("(max-width: 480px)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes


/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
