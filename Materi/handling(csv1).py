import csv



print('materi 10')
print("_________________________")
 #buka file
file_path =  r"\Users\User\Desktop\Project IT\materi-kelas-a\pesan.txt"
file_pesan = open(file_path, 'r')
 #baca isi file 
isi_pesan = file_pesan.read()
 #tampilkan output isi pesan
print(f"ISI TEXT:{isi_pesan}")
 #tutup file
file_pesan.close()

#versi CSV
#buka file
file_pathjajan =  r"\Users\User\Desktop\Project IT\materi-kelas-a\jajan.csv"
# r (raw string) -> olah data string asli
file_jajan = open(file_pathjajan, 'r')# open () -> membuka file dari file path
#baca isi file 
isi_jajan = file_jajan.read()# baca file path
#tampilkan output isi pesan
print(f"ISI TABLE JAJAN:{isi_jajan}")
#tutup file
file_jajan.close()


print("-----appened csv file------")
jajan_baru = [6, "syahid", 100000]
print(f'jajan baru: {jajan_baru}')
# mode"a" -> appned (tambah data)
# new line -> tambah baris baru dengan teks kosong
# with.. as -> buka file dgn tutup otomatis
with open(file_pathjajan, 'a', newline="") as file_jajan:
     # aktifkan mode writer csv dari file target
     writer = csv.writer(file_jajan)
     writer.writerow(jajan_baru)