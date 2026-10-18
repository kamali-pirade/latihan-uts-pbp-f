const loadBooksButton = document.getElementById("load-books");
const bookStatus = document.getElementById("book-status");
const bookList = document.getElementById("book-list");

loadBooksButton.addEventListener("click", async () => {
    bookStatus.textContent = "TODO: lengkapi fetch_books.js";
    bookList.innerHTML = "";

    // TODO LATIHAN 04:
    // 1. fetch("/api/books/")
    // 2. periksa response.ok
    // 3. await response.json()
    // 4. buat <li> untuk setiap buku dengan createElement + textContent
    // 5. tangani error menggunakan try/catch
});

