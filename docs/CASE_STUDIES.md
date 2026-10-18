# Studi Kasus Diskusi

Tidak ada satu jawaban pendek untuk bagian ini. Gunakan bukti dari latihan,
materi kuliah, dan hasil diskusi kelompok.

## 1. AI dan data sensitif

Sebuah tim mengunggah source code, API key production, data pengguna, konfigurasi
database, dan Django `SECRET_KEY` ke layanan AI publik.

1. Risiko apa yang muncul?
2. Informasi apa yang harus dihapus atau disamarkan?
3. Bagaimana membuat contoh minimal yang tetap berguna bagi AI?
4. Siapa yang bertanggung jawab memverifikasi kode hasil AI?

## 2. Memilih web atau mobile

Universitas membutuhkan sistem presensi lintas perangkat, tetapi beberapa kelas
memiliki jaringan tidak stabil dan presensi mungkin membutuhkan kamera serta lokasi.

1. Platform apa yang dipilih?
2. Kebutuhan mana yang paling menentukan keputusan?
3. Apa trade-off biaya, maintenance, offline support, dan device features?
4. Apakah solusi gabungan diperlukan?

## 3. Session dan cookie di komputer umum

Pengguna menutup tab pada aplikasi lain tanpa mengakhiri sesi. Pengguna berikutnya
membuka situs yang sama dan akun sebelumnya masih aktif.

1. State apa yang mungkin masih tersedia?
2. Apa perbedaan session server dan cookie browser?
3. Apa tindakan pengguna dan developer yang dapat mengurangi risiko?

## 4. CORS untuk dashboard internal

API internal menggunakan konfigurasi berikut:

```text
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

1. Mengapa konfigurasi tersebut bermasalah?
2. Origin dan method apa yang sebenarnya dibutuhkan?
3. Bagaimana Principle of Least Privilege diterapkan?
4. Mengapa CORS tidak menggantikan authentication dan authorization?

## 5. Alur pencarian toko buku

Pengguna mengetik judul, JavaScript mengirim request, Django mencari data, server
mengembalikan JSON, dan JavaScript memperbarui DOM.

1. Jelaskan tanggung jawab URL, view, model, dan JavaScript.
2. Di mana loading, empty, dan error state ditangani?
3. Di mana debounce digunakan?
4. Bagaimana mencegah input berbahaya ditampilkan sebagai HTML?

