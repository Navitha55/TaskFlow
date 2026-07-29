const themeToggle = document.getElementById("theme-toggle");
const savedTheme = localStorage.getItem("theme");
if (savedTheme === "dark") {
    document.body.classList.add("dark");
}
function updateThemeIcon() {
    if (!themeToggle) {
        return;
    }
    if (document.body.classList.contains("dark")) {
        themeToggle.textContent = "🔆";
    } else {
        themeToggle.textContent = "🌙";
    }
}

updateThemeIcon();

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        const isDark =
            document.body.classList.contains("dark");
        localStorage.setItem(
            "theme",
            isDark ? "dark" : "light"
        );
        updateThemeIcon();
    });
}

const slides = document.querySelector(".slides");
const cards = document.querySelectorAll(".scroll-card");
const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");

if (
    slides &&
    cards.length > 0 &&
    leftArrow &&
    rightArrow
) {

    let index = 0;
    let intervalId = null;
    const totalCards = cards.length;
    function showCard() {
        slides.style.transition =
            "transform 0.6s ease";
        slides.style.transform =
            `translateX(-${index * 100}%)`;
        updateArrows();
    }
    function updateArrows() {
        leftArrow.disabled = index === 0;
        rightArrow.disabled =
            index === totalCards - 1;
    }
    function autoSlide() {
        index++;
        if (index >= totalCards) {
            index = 0;
        }
        showCard();
    }
    function startAutoSlide() {
        stopAutoSlide();
        intervalId =
            setInterval(autoSlide, 4000);
    }
    function stopAutoSlide() {
        if (intervalId !== null) {
            clearInterval(intervalId);
            intervalId = null;
        }
    }
    rightArrow.addEventListener("click", () => {
        if (index < totalCards - 1) {
            index++;
            showCard();
        }
    });
    leftArrow.addEventListener("click", () => {
        if (index > 0) {
            index--;
            showCard();
        }
    });
    slides.addEventListener("mouseenter", () => {
        stopAutoSlide();
    });
    slides.addEventListener("mouseleave", () => {
        startAutoSlide()
    });
    showCard();
    startAutoSlide();
}

function togglePassword(inputId, button) {

    const passwordInput = document.getElementById(inputId);

    if (passwordInput.type === "password") {

        passwordInput.type = "text";
        button.textContent = "🫣";

    } else {

        passwordInput.type = "password";
        button.textContent = "🤫";

    }

}