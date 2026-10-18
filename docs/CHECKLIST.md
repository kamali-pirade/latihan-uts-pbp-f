# Checklist Eksperimen

Isi checklist hanya setelah dapat menunjukkan bukti dari output, DevTools, shell,
atau test. Jangan mencentang hanya karena kode terlihat benar.

## Persiapan

- [ ] Virtual environment aktif.
- [ ] Dependency berhasil dipasang.
- [ ] `python manage.py migrate` berhasil.
- [ ] `python manage.py seed_latihan` berhasil.
- [ ] `python manage.py check` tidak menemukan masalah.
- [ ] Smoke test lulus.

## Latihan 01 - CSS Selector

- [ ] Mengaktifkan `article p` dan mencatat seluruh elemen yang cocok.
- [ ] Mengaktifkan `article > p` dan menjelaskan direct child.
- [ ] Mengaktifkan `h2 + p` dan menjelaskan adjacent sibling.
- [ ] Menggabungkan ketiganya dan memeriksa rule pemenang di DevTools.

## Latihan 02 - URL, View, Template

- [ ] `/latihan/greeting/Budi/` menghasilkan `Halo, Budi!`.
- [ ] Mengganti nama pada URL mengubah output.
- [ ] Tidak melakukan hard-code nama dalam template.
- [ ] `test_latihan02_greeting` lulus.

## Latihan 03 - Django ORM

- [ ] Menjalankan `all()`.
- [ ] Menjalankan `filter(stock__gt=0)`.
- [ ] Menjelaskan hasil `filter(pk=999)`.
- [ ] Menjelaskan hasil `get(pk=999)`.
- [ ] Menjelaskan kapan menggunakan `get()` dan `filter()`.

## Latihan 04 - Fetch dan DOM

- [ ] Tombol memicu GET `/api/books/`.
- [ ] `response.ok` diperiksa.
- [ ] Response JSON terlihat di Network.
- [ ] Daftar dibuat menggunakan DOM.
- [ ] Error state tersedia.

## Latihan 05 - Debounce

- [ ] Counter input bertambah pada setiap karakter.
- [ ] Sebelum perbaikan, counter handler sama dengan input.
- [ ] Setelah perbaikan, handler berjalan sekali setelah berhenti mengetik.
- [ ] Dapat menjelaskan fungsi `clearTimeout()`.

## Latihan 06 - Debug Fetch

- [ ] Menemukan error awal di Console.
- [ ] Menambahkan `await` pada operasi yang tepat.
- [ ] Memeriksa `response.ok`.
- [ ] Mode normal menampilkan profil.
- [ ] Simulasi 500 menampilkan error yang mudah dipahami.

## Latihan 07 - ModelForm

- [ ] Form terikat pada `request.POST` saat POST.
- [ ] `is_valid()` benar-benar dipanggil.
- [ ] `save()` benar-benar dipanggil.
- [ ] Input tidak valid menampilkan error.
- [ ] `test_latihan07_product_form` lulus.

## Latihan 08 - Struktur Tabel

- [ ] Memiliki `thead` dan `tbody`.
- [ ] Setiap kumpulan cell dibungkus `tr`.
- [ ] Header menggunakan `th`; data menggunakan `td`.
- [ ] Tombol berhasil menambahkan baris tanpa error.

## Latihan 09 - Object Authorization

- [ ] Identitas simulasi dipilih melalui parameter `as_user`.
- [ ] Alice dapat membuka dokumen Alice.
- [ ] Alice tidak dapat membuka dokumen Bob dengan mengganti URL.
- [ ] Akses tidak sah menghasilkan 404.
- [ ] `test_latihan09_document_access` lulus.

## Latihan 10 - Event Listener

- [ ] Menjelaskan mengapa NodeList tidak memiliki `addEventListener()`.
- [ ] Versi iterasi berhasil.
- [ ] Versi event delegation berhasil.
- [ ] Dapat menjelaskan `event.target` atau `closest()`.

## Latihan 11 - Session dan Cookie

- [ ] Menemukan `sessionid` di browser.
- [ ] Menemukan `latihan_theme` beserta masa berlakunya.
- [ ] Menghapus cookie dan mengamati request berikutnya.
- [ ] Tombol reset menghapus state demo.
- [ ] Dapat membedakan data session dengan session identifier.

## Latihan 12 - Alur Pencarian

- [ ] Query di-encode dengan `encodeURIComponent()`.
- [ ] Request terlihat pada Network.
- [ ] Loading, success, empty, dan error state tersedia.
- [ ] Hasil dirender dengan DOM.
- [ ] Debounce 500 ms bekerja.
- [ ] Dapat menjelaskan alur browser → URL → view → model → JSON → DOM.

