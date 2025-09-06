import json

file_path = r"C:\Python Basic\Tugas\json_api\dataset.json"

with open(file_path, "r") as file_materi:
    data_materi=json.load(file_materi)

print(data_materi)

total_pinjam = 0
belum_kembali = 0

print("Belum kembali:")
for anggota in data_materi["anggota"]:
    for buku_Pinjaman in anggota["pinjam"]:
        total_pinjam += 1
        if buku_Pinjaman["kembali"] == False:  
            belum_kembali += 1
            print(f"- {anggota['nama']} : {buku_Pinjaman['judul']} ({buku_Pinjaman['tanggal']})")

print(f"Total dipinjam: {total_pinjam} | Belum kembali: {belum_kembali}")
  






