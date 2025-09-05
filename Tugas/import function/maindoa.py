import doa_harian


doa_harian.doa_bercermin()


doa_harian.doa_mau_mkan()

doa_harian.doa_selesai_makan()

doa_harian.doa_mau_turu()


doa_harian.doa_bangun_turu()

import hitung_uang
uang_jajan = [ 20000, 35000, 30000, 21000, 34000,]

print(hitung_uang.tambah_lima_rebu(uang_jajan))

import ranking
nilai =[75, 90, 60, 88, 100,55]
print("mengurutkan nilai:", ranking.urutkan_nilai(nilai))

print("nilai trtinggi:", ranking.nilai_tertinggi(nilai))
print("nilai terendah:", ranking.nilai_terendah(nilai))


import emoji
mood = ["senang", "biasa", "sedih", "semangat"]
print(emoji.convert_mood(mood))