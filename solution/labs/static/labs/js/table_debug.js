const addRowButton = document.getElementById("add-row");
const tableStatus = document.getElementById("table-status");

addRowButton.addEventListener("click", () => {
    // tbody tersedia secara eksplisit pada HTML, bukan hanya hasil koreksi parser browser.
    const tableBody = document.querySelector("#product-table tbody");

    try {
        tableBody.insertAdjacentHTML(
            "beforeend",
            "<tr><td>Mouse</td><td>150000</td></tr>",
        );
        tableStatus.textContent = "Baris berhasil ditambahkan.";
    } catch (error) {
        console.error(error);
        tableStatus.textContent = `Gagal: ${error.message}`;
    }
});
