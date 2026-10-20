# Pertemuan 10 - String dan Pengolahan Teks

Nama : Siti Nurhasanah  
NIM  : 2225250073   
Kelas: 3B  

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

Jalankan program dengan perintah berikut:

python3 tugas/normalisasi_data_mahasiswa.py


## Algoritma

1. Membaca input nama mahasiswa.
2. Membaca input kode kelas.
3. Membersihkan nama menggunakan `strip()`.
4. Mengubah format nama menjadi Title Case menggunakan `title()`.
5. Memecah nama menjadi beberapa kata menggunakan `split()`.
6. Mengambil huruf pertama dari setiap kata untuk membuat inisial.
7. Membersihkan kode kelas menggunakan `strip()`.
8. Mengubah kode kelas menjadi huruf kapital menggunakan `upper()`.
9. Memisahkan bagian kode kelas menggunakan `split()`.
10. Menggabungkan kembali bagian kode kelas menggunakan tanda hubung (`-`) dengan `join()`.
11. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

## Test Case

| Input Nama | Input Kode Kelas | Hasil yang Diharapkan |
|------------|------------------|-----------------------|
| aan hendrayana | pmat a 2026 | Nama: Aan Hendrayana, Kode: PMAT-A-2026, Inisial: AH |
| fATHIYYAH mUTHMAINNAH | kelas b | Nama: Fathiyyah Muthmainnah, Kode: KELAS-B, Inisial: FM |
| BUDI | pmtk 01 | Nama: Budi, Kode: PMTK-01, Inisial: B |
| siti nur aisyah | kelas c | Nama: Siti Nur Aisyah, Kode: KELAS-C, Inisial: SNA |

## Hasil Pengujian

| No | Input Nama | Input Kode | Hasil Aktual | Status |
|----|------------|------------|--------------|--------|
| 1 | aan hendrayana | pmat a 2026 | AH, PMAT-A-2026 | Berhasil |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | FM, KELAS-B | Berhasil |
| 3 | BUDI | pmtk 01 | B, PMTK-01 | Berhasil |
| 4 | siti nur aisyah | kelas c | SNA, KELAS-C | Berhasil |


## Refleksi

Masalah yang ditemukan adalah data masukan sering mengandung spasi berlebih dan penggunaan huruf besar-kecil yang tidak konsisten. Solusi yang digunakan adalah membersihkan data dengan `strip()`, menyeragamkan penulisan nama menggunakan `title()`, serta menyeragamkan kode kelas menggunakan `upper()`. Dengan demikian data menjadi lebih rapi dan mudah diproses.
