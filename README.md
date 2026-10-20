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
| aan hendrayana | pmat a 2026 | Nama: Aan Hendrayana, Kode: PMAT-A-2026, Jumlah Kata: 2, Inisial: AH |
| siti nurhasanah | pmat b 2026 | Nama: Siti Nurhasanah, Kode: PMAT-B-2026, Jumlah Kata: 2, Inisial: SN |
| muhammad rizki pratama | pmat c 2026 | Nama: Muhammad Rizki Pratama, Kode: PMAT-C-2026, Jumlah Kata: 3, Inisial: MRP |

## Hasil Pengujian

| No | Input Nama | Input Kode | Hasil Aktual | Status |
|----|------------|------------|--------------|--------|
| 1 | aan hendrayana | pmat a 2026 | AH, PMAT-A-2026 | Berhasil |
| 2 | siti nurhasanah | pmat b 2026 | SN, PMAT-B-2026 | Berhasil |
| 3 | muhammad rizki pratama | pmat c 2026 | MRP, PMAT-C-2026 | Berhasil |

## Refleksi

Masalah yang ditemukan adalah data masukan sering mengandung spasi berlebih dan penggunaan huruf besar-kecil yang tidak konsisten. Solusi yang digunakan adalah membersihkan data dengan `strip()`, menyeragamkan penulisan nama menggunakan `title()`, serta menyeragamkan kode kelas menggunakan `upper()`. Dengan demikian data menjadi lebih rapi dan mudah diproses.
