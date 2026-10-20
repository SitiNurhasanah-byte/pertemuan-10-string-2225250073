def normalisasi_nama(nama):
    return nama.strip().title()

def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial

def normalisasi_kode(kode):
    kode = kode.strip().upper()
    bagian = kode.split()
    return "-".join(bagian)

# Input
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

# Output
print("\nHasil Normalisasi")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Inisial     :", inisial)