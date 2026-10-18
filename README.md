# PBP UTS Latihan Eksperimen

Repository ini berisi dua project Django yang dapat dijalankan secara terpisah:

| Folder | Kegunaan |
|---|---|
| [`template/`](template/) | Starter project untuk dikerjakan mahasiswa. Beberapa bagian sengaja mengandung TODO, bug, atau celah authorization. |
| [`solution/`](solution/) | Versi pembanding yang seluruh latihannya sudah diperbaiki dan diberi komentar penjelasan. |

Kerjakan `template/` terlebih dahulu. Gunakan `solution/` setelah melakukan
eksperimen sendiri untuk membandingkan implementasi dan alasannya.

## Menjalankan template

```bash
cd template
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py runserver
```

## Menjalankan solution

Hentikan server template, lalu buka terminal baru:

```bash
cd solution
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py test
python manage.py runserver
```

Untuk Windows PowerShell, aktivasi environment menggunakan:

```powershell
.venv\Scripts\Activate.ps1
```

Kedua project memakai URL <http://127.0.0.1:8000/>. Jalankan satu project pada
satu waktu agar port tidak bentrok.

## Akun latihan

- `alice / latihan123`
- `bob / latihan123`

Akun tersebut dibuat oleh `python manage.py seed_latihan` dan hanya ditujukan
untuk eksperimen lokal.
