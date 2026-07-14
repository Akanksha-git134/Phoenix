const textarea = document.getElementById("job-description");
const counter = document.getElementById("char-count");

textarea.addEventListener("input", () => {

    counter.textContent =
        `Characters: ${textarea.value.length}`;

});

const themeBtn = document.querySelector(".theme-btn");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    themeBtn.textContent =
        document.body.classList.contains("dark-mode")
            ? "☀️"
            : "🌙";

});

const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click", () => {

    navLinks.classList.toggle("active");

    menuBtn.textContent =
        navLinks.classList.contains("active")
            ? "✕"
            : "☰";

});

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");
        menuBtn.textContent = "☰";

    });

});