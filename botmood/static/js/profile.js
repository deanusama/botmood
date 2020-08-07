var btn = document.querySelector(".edit-password-text");
var hiddenForm = document.querySelector(".form-group-hidden")

btn.addEventListener("click", function(){
    hiddenForm.classList.toggle("group-active");
})

var rotate = document.querySelector(".arrow")
var container = document.querySelector(".form-container")
rotate.addEventListener("click",function(){
    container.classList.toggle("form-container-hidden")
    rotate.classList.toggle("arrow-up")
})  



var edit =  document.querySelector(".edit") 
var courses =  document.querySelector(".courses") 
var bookmarks =  document.querySelector(".bookmarks")
var form = document.querySelector(".form-container")
var coursesSection = document.querySelector(".my-course-section")
var favorite = document.querySelector(".favorite-courses")

edit.addEventListener("click", ()=>{
    courses.classList.remove("active")
    edit.classList.add("active")
    bookmarks.classList.remove("active")
    coursesSection.style.display = "none"
    form.style.display = "block"
    favorite.style.display = "none"
})

courses.addEventListener("click", ()=>{
    courses.classList.add("active")
    edit.classList.remove("active")
    bookmarks.classList.remove("active")
    coursesSection.style.display = "block"
    form.style.display = "none"
    favorite.style.display = "none"
})

bookmarks.addEventListener("click", ()=>{
    courses.classList.remove("active")
    edit.classList.remove("active")
    bookmarks.classList.add("active")
    coursesSection.style.display = "none"
    form.style.display = "none"
    favorite.style.display = "block"
})
