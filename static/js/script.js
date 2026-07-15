window.history.scrollRestoration = "manual";
window.addEventListener("load", () => {
    window.scrollTo(0, 0);
});
const textarea = document.getElementById("job-description");
const counter = document.getElementById("char-count");

function updateCounter(){

    const count = textarea.value.length;

    counter.textContent = `Characters: ${count}`;

    if(count > 40000){

        counter.style.color="#e74c3c";

    }

    else if(count > 25000){

        counter.style.color="#f39c12";

    }

    else{

        counter.style.color="";

    }

}

updateCounter();

const clearBtn = document.getElementById("clearBtn");

clearBtn.addEventListener("click", () => {

    textarea.value = "";
    updateCounter();
    textarea.focus();

});

textarea.addEventListener("input", updateCounter);

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
