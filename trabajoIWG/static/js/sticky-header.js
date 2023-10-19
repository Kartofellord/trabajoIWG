document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', stick);

    var stickyHeader = document.getElementById("stickyHeader");
    var sticky = stickyHeader.offsetTop;

    function stick() {
        if (window.scrollY >= sticky) {
        stickyHeader.classList.add("sticky");
        } else {
        stickyHeader.classList.remove("sticky");
        }
    }
})