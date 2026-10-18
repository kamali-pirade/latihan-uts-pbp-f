const buttonContainer = document.getElementById("button-container");

// Event delegation cukup memasang satu listener pada parent. closest() memastikan
// klik pada isi button tetap menemukan .remove-button yang sesuai.
buttonContainer.addEventListener("click", (event) => {
    const button = event.target.closest(".remove-button");
    if (!button || !buttonContainer.contains(button)) {
        return;
    }

    button.remove();
    document.getElementById("event-status").textContent =
        "Satu tombol dihapus melalui event delegation.";
});
