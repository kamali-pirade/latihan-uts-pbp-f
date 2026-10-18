const loadBooksButton = document.getElementById("load-books");
const bookStatus = document.getElementById("book-status");
const bookList = document.getElementById("book-list");

loadBooksButton.addEventListener("click", async () => {
    bookStatus.textContent = "Memuat buku...";
    bookList.innerHTML = "";

    try {
        // await pertama menunggu response HTTP, bukan langsung data JSON.
        const response = await fetch("/api/books/");
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        // Body response juga dibaca secara asynchronous.
        const books = await response.json();

        books.forEach((book) => {
            const item = document.createElement("li");
            // textContent tidak menafsirkan data API sebagai HTML.
            item.textContent = `${book.title} — ${book.author}`;
            bookList.appendChild(item);
        });
        bookStatus.textContent = `${books.length} buku berhasil dimuat.`;
    } catch (error) {
        console.error(error);
        bookStatus.textContent = `Gagal memuat buku: ${error.message}`;
    }
});
