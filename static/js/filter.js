
        // ------------------- Category Filter
        $(".default_option").click(function () {
            $(this).parent().toggleClass("active");
        })

        $(".select_ul li").click(function () {
            var currentele = $(this).html();
            $(".default_option li").html(currentele);
            $(this).parents(".select_wrap").removeClass("active");
        })

        // ------------------------------- See More Button
        var topics = document.querySelectorAll(".category");
        var loadBtn = document.querySelector(".see-more-text");


        if (topics.length > 5) {
            loadBtn.style.display = "block"
            for (let i = 5; i < topics.length; i++) {
                topics[i].style.display = "none"
            }
            loadBtn.addEventListener("click", function () {
                for (let i = 5; i < topics.length; i++) {
                    topics[i].style.display = "block"
                }
                loadBtn.style.display = "none"
            });
        }


        var category = document.querySelector(".dropdown-heading");
        var hiddenCategory = document.querySelector(".categories");
        var arrow = document.querySelector(".img-div");
        category.addEventListener("click", function(){
            hiddenCategory.classList.toggle("hidden")
            arrow.classList.toggle("rotated")
        })
