const buttons = document.querySelectorAll(".remove-button");

// TODO LATIHAN 10: NodeList tidak memiliki addEventListener.
// Perbaikan pertama: iterasikan buttons dan pasang listener pada setiap button.
// Perbaikan kedua: pasang satu listener pada #button-container (event delegation).
buttons.addEventListener("click", function () {
    this.remove();
});

