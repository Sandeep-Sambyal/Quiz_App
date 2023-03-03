console.log("main.js loaded");
var modBtn = [...document.getElementsByClassName("modal-button")];  //converting to Array
var modTitle = document.getElementsByClassName("modal-title")[0];
var strtBtn = document.getElementById("starttest");

var url = window.location.href;

modBtn.forEach(element => element.addEventListener("click", () =>{
    // console.log("TEST",element.dataset['quiz']);
    modTitle.innerHTML = element.getAttribute("data-quiz");;

    strtBtn.addEventListener("click", ()=>{
        console.log(element.getAttribute("data-pk"));
        window.location.href = url+element.getAttribute("data-pk");
    })
}
));