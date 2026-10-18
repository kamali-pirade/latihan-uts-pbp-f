const productSearch = document.getElementById("product-search");
const searchStatus = document.getElementById("search-flow-status");
const searchResults = document.getElementById("search-results");

async function searchProducts(keyword) {
    searchStatus.textContent = `TODO: cari "${keyword}" melalui API`;

    // TODO LATIHAN 12:
    // 1. tampilkan loading state
    // 2. fetch(`${window.PRODUCTS_API_URL}?q=${encodeURIComponent(keyword)}`)
    // 3. periksa response.ok lalu parse JSON
    // 4. render data.results dengan createElement + textContent
    // 5. tampilkan empty state jika results kosong
    // 6. tampilkan error state jika request gagal
}

function debounce(func, delay) {
    let timer;
    return function (...args) {
        // TODO LATIHAN 12: implementasikan debounce 500 ms.
        func.apply(this, args);
    };
}

const debouncedProductSearch = debounce((event) => {
    searchProducts(event.target.value.trim());
}, 500);

productSearch.addEventListener("input", debouncedProductSearch);

