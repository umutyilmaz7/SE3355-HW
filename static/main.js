document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector("input[name='search']"); 

    searchInput.addEventListener("input", function () {
        if (searchInput.value.trim() === "") {
            window.location.href = "/";
        }
    });
});
