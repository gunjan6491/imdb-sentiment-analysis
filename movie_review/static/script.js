const reviewInput = document.getElementById("review");

const counter = document.getElementById("counter");

const form = document.getElementById("reviewForm");

const button = document.getElementById("analyzeBtn");

// Character counter
reviewInput.addEventListener("input", function () {
    counter.textContent = this.value.length + " characters";
});

// Loading effect on submit
form.addEventListener("submit", function () {

    if (reviewInput.value.trim() === "") {
        alert("Please enter a movie review!");
        return;
    }

    button.textContent = "Analyzing...";
    button.disabled = true;

});