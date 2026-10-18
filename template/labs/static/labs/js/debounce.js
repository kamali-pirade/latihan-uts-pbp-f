const searchBox = document.getElementById("search-box");
const rawCountElement = document.getElementById("raw-count");
const handledCountElement = document.getElementById("handled-count");
const searchOutput = document.getElementById("search-output");

let rawCount = 0;
let handledCount = 0;

function debounce(func, delay) {
    let timer;

    return function (...args) {
        // TODO LATIHAN 05:
        // clearTimeout(timer);
        // timer = setTimeout(() => func.apply(this, args), delay);

        // Starter sengaja menjalankan fungsi langsung agar counter dapat dibandingkan.
        func.apply(this, args);
    };
}

function handleSearch(event) {
    handledCount += 1;
    handledCountElement.textContent = handledCount;
    searchOutput.textContent = `Mencari: ${event.target.value}`;
}

const debouncedSearch = debounce(handleSearch, 500);

searchBox.addEventListener("input", (event) => {
    rawCount += 1;
    rawCountElement.textContent = rawCount;
    debouncedSearch(event);
});

