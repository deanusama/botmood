let click = document.querySelector(".fa-search");
let borderRow = document.querySelector(".navbar-header__row");
let hidden = document.querySelector(".search-row-container");
let body = document.querySelector("body");
let empty = document.querySelector(".empty-container");

click.addEventListener("click", function(){
    borderRow.classList.toggle("row-bordered")
    hidden.classList.toggle("collapsed")
    empty.classList.toggle("hidden-container")
})

empty.addEventListener("click", function(){
    borderRow.classList.toggle("row-bordered")
    hidden.classList.toggle("collapsed")
    empty.classList.toggle("hidden-container")
})


// responsive navbar

let trigger = document.querySelector(".burger");
let nav = document.querySelector(".main-nav");
let navLinks = document.querySelectorAll(".nav-item")

trigger.addEventListener("click", function(){
    nav.classList.toggle("active")
    trigger.classList.toggle("toggle")
        // Animation
        navLinks.forEach((link, index) =>{
            if(link.style.animation){
                link.style.animation = ""
            }else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/ 7 +0.3}s`   
            }
    })
    
})
