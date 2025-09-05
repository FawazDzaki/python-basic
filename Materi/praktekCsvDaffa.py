import csv

file_path =r"C:\Users\User\Desktop\Project IT\materi-kelas-a\kelass.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)# buat nge skip(gak ikut ke print) judulnya
    read = csv.reader(file_baru)# baca n ambil data
    list_read = list(read)

    print('SEMUA DATA')
    print("_"*20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        kelas = baris[2]
        print(f"{nomor} | {nama} | {kelas}")

    #   TAMBAH DATA
with open(file_path, "a", newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5", "faiz", "18"])