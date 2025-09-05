import csv
# tambah kan module csv dengan import
print("-----Materi 11- file handling part 2")
print("-----update CSV-----")
file_pathjajan =  r"\Users\User\Desktop\Project IT\materi-kelas-a\jajan.csv"
# baca semua file -> ekstrak data -> buat data baru
# tulis ulang semua isi barisnya dengan mode "w"
# siapkan data jajan kosong untuk menampung data dari csv ke list
data_jajan = []
with open(file_pathjajan, 'r') as file_jajan:
    # csv.reader() membaca isi file csv
    isi_tabel_jajan = csv.reader(file_jajan)
    # ekstrak semua data dengan for loop
    for item_jajan in isi_tabel_jajan:
        print(item_jajan)
        # tambah item ke list data jajan
        data_jajan.append(item_jajan)


# 1. baca seluruh data =
# with open(file_pathjajan, 'r') as file_jajan:...

# 2. mengubah atau membuat data baru
for item in data_jajan:
    print(f"Prose item no => {item[0]}")
    print(item)
    print("_____________")
    # jika kolom nama(index 1) adalah "x nama"
    if item[1] == "thufail":
        uang_jajan_baru = 15000
        print(f" data target ketemu, ubah uang jajannya ke{uang_jajan_baru}")
        # ganti kolom uang (index 2) dengan nilai baru
    print("_____loop end_____")

# 3.menghapus data
# del data_jajan[2]
# print(f'DATA JAJAN TERKINI: {data_jajan}')

# # 4. tulis ulng data dengan mode "w" --> write
# with open(file_pathjajan, 'w', newline="") as file_jajan:
# # aktifkan mode writer csv dari file target
#     writer = csv.writer(file_jajan)
#     # writerows() -> tulis sekali banyak
#     writer.writerow(data_jajan)

    


