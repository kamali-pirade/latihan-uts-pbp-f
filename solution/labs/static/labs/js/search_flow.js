const productSearch = document.getElementById("product-search");
const searchStatus = document.getElementById("search-flow-status");
const searchResults = document.getElementById("search-results");

async function searchProducts(keyword) {
    searchResults.innerHTML = "";

    if (!keyword) {
        searchStatus.textContent = "Mulai mengetik untuk mencari.";
        return;
    }

    searchStatus.textContent = `Mencari "${keyword}"...`;

    try {
        const url = `${window.PRODUCTS_API_URL}?q=${encodeURIComponent(keyword)}`;
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        if (data.results.length === 0) {
            searchStatus.textContent = "Produk tidak ditemukan.";
            return;
        }

        data.results.forEach((product) => {
            const card = document.createElement("article");
            card.className = "panel";

            const title = document.createElement("h2");
            title.textContent = product.name;

            const detail = document.createElement("p");
            detail.textContent = `Stok ${product.stock} · Harga Rp${product.price}`;

            card.append(title, detail);
            searchResults.appendChild(card);
        });
        searchStatus.textContent = `${data.results.length} produk ditemukan.`;
    } catch (error) {
        console.error(error);
        searchStatus.textContent = `Pencarian gagal: ${error.message}`;
    }
}

function debounce(func, delay) {
    let timer;
    return function (...args) {
        // Hanya request dari input terakhir yang dijalankan setelah 500 ms.
        clearTimeout(timer);
        timer = setTimeout(() => func.apply(this, args), delay);
    };
}

const debouncedProductSearch = debounce((event) => {
    searchProducts(event.target.value.trim());
}, 500);

productSearch.addEventListener("input", debouncedProductSearch);
