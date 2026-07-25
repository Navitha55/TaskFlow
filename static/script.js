const slides = document.querySelector(".slides");
const cards = document.querySelectorAll(".scroll-card");

const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");

const themeToggle = document.getElementById("theme-toggle");

let index = 0;
let intervalId = null;

const totalCards = cards.length;


// ==========================================
// SHOW CARD
// ==========================================

function showCard() {

    slides.style.transition = "transform 0.6s ease";

    slides.style.transform =
        `translateX(-${index * 100}%)`;

    updateArrows();
}


// ==========================================
// UPDATE ARROW STATE
// ==========================================

function updateArrows() {

    // Disable LEFT arrow at first card
    leftArrow.disabled = index === 0;

    // Disable RIGHT arrow at last card
    rightArrow.disabled = index === totalCards - 1;

}


// ==========================================
// AUTO SLIDE
// ==========================================

function autoSlide() {

    index++;

    // After Card 6, return to Card 1
    if (index >= totalCards) {

        index = 0;

    }

    showCard();

}


// ==========================================
// START AUTO SLIDE
// ==========================================

function startAutoSlide() {

    stopAutoSlide();

    intervalId = setInterval(autoSlide, 4000);

}


// ==========================================
// STOP AUTO SLIDE
// ==========================================

function stopAutoSlide() {

    if (intervalId !== null) {

        clearInterval(intervalId);

        intervalId = null;

    }

}


// ==========================================
// RIGHT ARROW
// LEFT → RIGHT CARD NAVIGATION
// ==========================================

rightArrow.addEventListener("click", () => {

    if (index < totalCards - 1) {

        index++;

        showCard();

    }

});


// ==========================================
// LEFT ARROW
// RIGHT → LEFT CARD NAVIGATION
// ==========================================

leftArrow.addEventListener("click", () => {

    if (index > 0) {

        index--;

        showCard();

    }

});


// ==========================================
// PAUSE AUTO SLIDE WHILE READING
// ==========================================

slides.addEventListener("mouseenter", () => {

    stopAutoSlide();

});


slides.addEventListener("mouseleave", () => {

    startAutoSlide();

});


// ==========================================
// DARK / LIGHT THEME
// ==========================================

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {

        themeToggle.textContent = "☀️";

    } else {

        themeToggle.textContent = "🌙";

    }

});


// ==========================================
// INITIAL STATE
// ==========================================

showCard();

startAutoSlide();