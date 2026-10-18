const profileName = document.getElementById("profile-name");
const profileRole = document.getElementById("profile-role");
const profileStatus = document.getElementById("profile-status");

async function loadProfile(url) {
    profileStatus.textContent = "Memuat...";
    profileName.textContent = "-";
    profileRole.textContent = "-";

    try {
        // fetch mengembalikan Promise, sehingga harus ditunggu dengan await.
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        profileName.textContent = data.name;
        profileRole.textContent = data.role;
        profileStatus.textContent = "Berhasil.";
    } catch (error) {
        console.error(error);
        profileStatus.textContent = `Gagal: ${error.message}`;
    }
}

document.getElementById("load-profile").addEventListener("click", (event) => {
    loadProfile(event.currentTarget.dataset.url);
});

document.getElementById("load-error").addEventListener("click", (event) => {
    loadProfile(event.currentTarget.dataset.url);
});
