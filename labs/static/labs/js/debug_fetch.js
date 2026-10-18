const profileName = document.getElementById("profile-name");
const profileRole = document.getElementById("profile-role");
const profileStatus = document.getElementById("profile-status");

async function loadProfile(url) {
    profileStatus.textContent = "Memuat...";

    // TODO LATIHAN 06: kode berikut sengaja salah.
    // Tambahkan await, response.ok, dan try/catch.
    const response = fetch(url);
    const data = response.json();

    profileName.textContent = data.name;
    profileRole.textContent = data.role;
    profileStatus.textContent = "Berhasil.";
}

document.getElementById("load-profile").addEventListener("click", (event) => {
    loadProfile(event.currentTarget.dataset.url);
});

document.getElementById("load-error").addEventListener("click", (event) => {
    loadProfile(event.currentTarget.dataset.url);
});

