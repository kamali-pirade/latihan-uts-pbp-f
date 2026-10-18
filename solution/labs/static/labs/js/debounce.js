const searchBox = document.getElementById("search-box");
const rawCountElement = document.getElementById("raw-count");
const handledCountElement = document.getElementById("handled-count");
const searchOutput = document.getElementById("search-output");

let rawCount = 0;
let handledCount = 0;

function debounce(func, delay) {
    let timer;

    return function (...args) {
        // Setiap input baru membatalkan jadwal lama. Fungsi hanya dijalankan
        // setelah tidak ada input baru selama `delay` milidetik.
        clearTimeout(timer);
        timer = setTimeout(() => func.apply(this, args), delay);
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
