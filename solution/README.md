# PBP UTS Latihan Eksperimen — Solution

Folder ini adalah versi pembanding dari [`../template/`](../template/). Seluruh
TODO sudah diselesaikan dan bagian penting diberi komentar yang menjelaskan
alasan implementasinya.

Gunakan solution setelah mencoba template sendiri. Jangan hanya menyalin kode:
bandingkan perubahan, jalankan DevTools, lalu jelaskan mengapa hasilnya berubah.

## Setup macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py test
python manage.py runserver
```

## Setup Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py test
python manage.py runserver
```

Buka <http://127.0.0.1:8000/>. Jalankan template dan solution secara bergantian
karena keduanya menggunakan port 8000.

## Akun Latihan 09

- `alice / latihan123`
- `bob / latihan123`

Pada solution, Alice hanya dapat membuka dokumen Alice dan akan memperoleh 404
ketika mencoba membuka dokumen Bob.

## Hasil yang perlu diamati

1. CSS menunjukkan perbedaan descendant, child, dan adjacent sibling selector.
2. Parameter nama pada URL diteruskan oleh view ke template.
3. Query ORM menampilkan data hasil seed.
4. Fetch memuat JSON dan membangun DOM menggunakan `textContent`.
5. Debounce menggabungkan input cepat menjadi satu pemanggilan.
6. Fetch membedakan response sukses dan HTTP error.
7. ModelForm melakukan binding, validasi, dan penyimpanan.
8. Tabel mempunyai struktur `thead` dan `tbody` yang valid.
9. Query dokumen menerapkan object-level authorization.
10. Event delegation menangani banyak tombol melalui satu listener.
11. Session dan cookie mempertahankan state antar-request.
12. Pencarian menghubungkan input, debounce, API, ORM, JSON, dan DOM.

Seluruh Django test harus lulus:

```bash
python manage.py test
```
