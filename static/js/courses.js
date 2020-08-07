const accordionItemHeaders = document.querySelectorAll(".accordion-item-header");

accordionItemHeaders.forEach(accordionItemHeader => {
    accordionItemHeader.addEventListener("click", event => {

        // Uncomment in case you only want to allow for the display of only one collapsed item at a time!

        const currentlyActiveAccordionItemHeader = document.querySelector(
            ".accordion-item-header.active");
        if (currentlyActiveAccordionItemHeader && currentlyActiveAccordionItemHeader !==
            accordionItemHeader) {
            currentlyActiveAccordionItemHeader.classList.toggle("active");
            currentlyActiveAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
        }

        accordionItemHeader.classList.toggle("active");
        const accordionItemBody = accordionItemHeader.nextElementSibling;
        if (accordionItemHeader.classList.contains("active")) {
            accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
        } else {
            accordionItemBody.style.maxHeight = 0;
        }

    });
});




// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
        copyClick.innerText = "Copy Link"
    }
}

var copyClick = document.querySelector(".copy-btn button")

copyClick.addEventListener("click", function () {
    var content = document.getElementById("link_Copied").innerHTML
    var el = document.createElement("textarea")

    copyClick.innerText = "Link Copied"
    el.value = content
    el.setAttribute = ("readonly", "")
    el.style = {
        position: "absolute",
        left: "-9999px"
    }
    document.querySelector("body").appendChild(el)
    el.select()
    document.execCommand('copy')
    document.querySelector("body").removeChild(el)
})



var contentBlocks = document.querySelectorAll(".course-content-block");
var loadBtn = document.querySelector(".load-more-btn");
var lessBtn = document.querySelector(".see-less-btn");
var btnHeading = document.querySelector(".load-more-heading");


if (contentBlocks.length > 5) {
    loadBtn.style.display = "block"
    loadBtn.innerHTML = +contentBlocks.length - 5 + " More Sections"
    loadBtn.style.fontSize = "1.2rem"
    loadBtn.style.textAlign = "center"
    loadBtn.style.fontFamily = "ProximaNova"
    loadBtn.style.fontWeight = "400"
    loadBtn.style.color = "#ff9d68"


    for (let i = 5; i < contentBlocks.length; i++) {
        contentBlocks[i].style.display = "none"
    }
    loadBtn.addEventListener("click", function () {
        for (let i = 5; i < contentBlocks.length; i++) {
            contentBlocks[i].style.display = "flex"
        }
        loadBtn.style.display = "none"
        lessBtn.style.display = "block"
    });

    lessBtn.addEventListener("click", function () {
        for (let i = contentBlocks.length - 1; i > 4; i--) {
            contentBlocks[i].style.display = "none"
        }
        lessBtn.style.display = "none"
        loadBtn.style.display = "block"
    });
}