import csv

file_path =r"C:\Users\User\Desktop\Project IT\Tugas\tugasCSV\keuangan.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)# buat nge skip(gak ikut ke print) judulnya
    read = csv.reader(file_baru)# baca n ambil data
    list_read = list(read)

    print('SEMUA DATA')
    print("_"*20)
    print("Tanggal | keterangan | kategori | jumlah")
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori= baris[2]
        jumlah = baris[3]
        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")