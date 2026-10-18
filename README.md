# PBP UTS Latihan Eksperimen

Repository starter untuk mempelajari materi UTS PBP melalui eksperimen mandiri.
Targetnya bukan sekadar mendapatkan output, tetapi memahami hubungan antara
HTML/CSS, JavaScript, HTTP, Django URL, view, template, model, form, session,
cookie, dan authorization.

> Jalankan, ubah, amati, lalu jelaskan alasan hasilnya.

## Yang tersedia

- 12 latihan yang dapat dibuka dari satu dashboard.
- Penanda `TODO LATIHAN ...` pada bagian yang harus diubah mahasiswa.
- API lokal sehingga latihan Fetch tidak bergantung pada internet.
- Data contoh yang dapat dibuat ulang dengan management command.
- Smoke test untuk memeriksa starter project.
- Challenge test untuk latihan Django.
- Checklist DevTools untuk eksperimen frontend.
- Lembar catatan eksperimen dan lima studi kasus diskusi.

## Persyaratan

- Python 3.11 atau lebih baru.
- Terminal/Command Prompt.
- Browser dengan Developer Tools.

## Setup macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py runserver
```

## Setup Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_latihan
python manage.py runserver
```

Buka <http://127.0.0.1:8000/>.

Latihan 09 menggunakan autentikasi Django agar eksperimen authorization dapat
dilakukan dengan pengguna yang benar-benar tercatat pada session:

- `alice / latihan123`
- `bob / latihan123`

Login melalui `/accounts/login/`, lalu buka `/latihan/documents/1/`. Coba ubah ID
dokumen untuk menguji apakah object-level authorization sudah benar.

## Cara mencari TODO

Dengan ripgrep:

```bash
rg -n "TODO LATIHAN" . -g '!*.sqlite3' -g '!.venv/**'
```

Atau dengan fitur pencarian global editor dan cari `TODO LATIHAN`.

Jangan menghapus komentar TODO sebelum eksperimen selesai dan sudah dicatat.

## Cara memeriksa project

### 1. Pemeriksaan konfigurasi

```bash
python manage.py check
```

### 2. Smoke test

Smoke test harus lulus sejak awal:

```bash
python manage.py test labs.tests.test_smoke
```

### 3. Challenge test

Challenge test memang sengaja gagal pada starter code. Jalankan setelah
memperbaiki TODO terkait:

```bash
python manage.py test labs.tests.test_latihan02_greeting
python manage.py test labs.tests.test_latihan07_product_form
python manage.py test labs.tests.test_latihan09_document_access
```

Setelah ketiganya lulus:

```bash
python manage.py test
```

Jangan mengubah test agar menjadi hijau. Perbaiki implementasinya.

### 4. Pemeriksaan frontend

Gunakan Developer Tools browser:

- **Elements → Styles**: selector CSS dan struktur tabel.
- **Console**: error JavaScript dan jumlah event.
- **Network**: URL, method, status HTTP, dan response JSON.
- **Application/Storage → Cookies**: `sessionid` dan `latihan_theme`.

Checklist lengkap tersedia di [docs/CHECKLIST.md](docs/CHECKLIST.md).

## Peta latihan

| Latihan | Topik | URL | File utama | Cara cek |
|---|---|---|---|---|
| 01 | CSS selector | `/latihan/css-selectors/` | `css_experiment.css` | Elements → Styles |
| 02 | URL, view, template | `/latihan/greeting/Budi/` | `views.py`, `greeting.html` | `test_latihan02_greeting` |
| 03 | Django ORM | `/latihan/orm/` | `models.py` | Django shell |
| 04 | Fetch dan DOM | `/latihan/fetch-books/` | `fetch_books.js` | Network + Elements |
| 05 | Debounce | `/latihan/debounce/` | `debounce.js` | Counter pemanggilan |
| 06 | Debug Fetch | `/latihan/debug-fetch/` | `debug_fetch.js` | Console + Network |
| 07 | ModelForm | `/latihan/product-form/` | `views.py` | `test_latihan07_product_form` |
| 08 | Struktur tabel | `/latihan/table-debug/` | `table_debug.html` | Elements + Console |
| 09 | Object authorization | `/latihan/documents/<id>/` | `views.py` | `test_latihan09_document_access` |
| 10 | Event listener | `/latihan/events/` | `event_debug.js` | Console |
| 11 | Session dan cookie | `/latihan/session-cookie/` | `views.py` | Application → Cookies |
| 12 | Alur pencarian | `/latihan/search-flow/` | `search_flow.js` | Network + DOM |

## Urutan belajar yang disarankan

1. Latihan 01 untuk CSS dan DevTools.
2. Latihan 02–03 untuk alur Django dan ORM.
3. Latihan 04–06 untuk asynchronous JavaScript.
4. Latihan 07–09 untuk form dan keamanan.
5. Latihan 10–12 untuk event, state, dan integrasi penuh.

Catat setiap eksperimen menggunakan
[docs/EXPERIMENT_LOG.md](docs/EXPERIMENT_LOG.md). Setelah latihan selesai,
diskusikan [docs/CASE_STUDIES.md](docs/CASE_STUDIES.md).

## Git workflow opsional

Jika ingin melatih penggunaan branch, buat satu branch untuk satu latihan:

```bash
git switch -c latihan/04-fetch-dom
git add .
git commit -m "Complete fetch and DOM experiment"
```

Branch dibuat berdasarkan task/latihan, bukan branch permanen berdasarkan nama orang.

