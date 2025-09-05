print("materi 6 - python data structure")
print("_________________")
#list [] (berurutan, bisa diubah, boleh duplikat)
daftar_belanja = [
"gabin", # index 0
"naspad", 
"es teh",
"pisang",
]
print("isi tas belanja:", daftar_belanja)
print("item ke 1-:", daftar_belanja[0])
print("")

#append() menambah item baru ke akhir list
daftar_belanja.append("roti")
daftar_belanja.append("olive")
print("isi tas belanj skrg:", daftar_belanja)
print("item ke 5", daftar_belanja[4])
print("")
print("")

#remove
daftar_belanja.remove("pisang")
print("isi tas belanja akhir:", daftar_belanja)
print("")
print("")

#klo pake index(gak pake str)
daftar_belanja.pop(0)
print('setelah di hapus pake pop:', daftar_belanja)
print("")
print("")

# nambah di index terserah
daftar_belanja.insert(3, "cabe")
print("setelah di tambah pake insert:", daftar_belanja)
print("")
print("")

#  cara mengubah data
daftar_belanja[1] = "nanas"
print("setelah diubah:", daftar_belanja)
print("")
print("")

#cara mengetahui panjang list
print(len(daftar_belanja))
print("")
print("")
# klo mau print 1 1 atau ada enternya:
for i in daftar_belanja:
    print(i)

for i in range(5):
 print("")
 print("")
 print("")

#print("______TUPLE______")
#tuple (berurutan, tidak bisa diubah, boleh duplikat)
#penulisannya menggunakan ()
ttl = ("Jakarta", 21, "november", 2009)
print("tgl lahir gw:", ttl)
#[no_index] akses data tuple
print("Tempat:", ttl[0])
print("Tanggal:", ttl[1])
print("Bulan:", ttl[2])
print("Tahun:", ttl[3])

print("bulan,tahun:", ttl[2:4])
#unpacking tuple ke variable lain
tempat_lahir, tgl_lahir, bula_lahir, tahun_lahir = ttl
print(tempat_lahir)
print(tgl_lahir)
print(bula_lahir)
print(tahun_lahir)
#manipulsai teks lanjutan
#menggabungkan dengan +:
jajananGw = ["gabin", "pisang"]
jajanLu = ['nasi', 'bakso']
jajananKita = jajananGw + jajanLu
print(jajananKita)
#jika dimasukan int pun tetap bisa

#list multi-dimensi
list_minuman = [
    ["kopi", 'susu', 'teh'],
    ["ayam", "bebek", "sapi"],  # 1
    ["esteh", "es jeruk", "es kopi"],  # 2
   ]
print(list_minuman[1][2])

for i in range(5):
    print("")


# # set -> {} <- tidak berurutan, berubah, tak boleh duplikat
gameAzka = {"valorant",'roblox', 'delta'}
gameZaky = {"minecraft", "roblox", "ML", "FF"}
gameAzka.add("minecraft")
gameZaky.add("roblox")
gameAzka.remove("valorant")

print("game azka:", gameAzka)
print("game zaky", gameZaky)
gameGabungan = gameAzka | gameZaky # | = or/atau
print("Daftar game:", gameGabungan)
 
for game in gameGabungan:
     print(game)
     print("---> Tranfer game", game, "Ke PS5")


for i in range(5):
     print("")



# dictionary (dict) -> {key/value} / {kunci/isi}/pemanggilannya tidak menggunakan index tapi dgn key
# -> berurutan, berubah, tidak duplikat
kamus_anime = {
    "bluelok": "isagi Ren",
    "demon_slayer": "tanjiro",
    "waifu:":{
        "one_piece": "big mom",
        "demon_slayer": "nezuko"
    }
    }
print("Kamus anime:", kamus_anime)
print("MC demon:", kamus_anime["demon_slayer"])
print("Waifu one piece:", kamus_anime["waifu:"]["one_piece"])
#nambah item baru dict : ["key"] = value
kamus_anime["naruto:"] = "shikamaru"
print("MC naruto:", kamus_anime["naruto:"])
print(kamus_anime)
#mengubah
kamus_anime["demon_slayer"] = "zinetsu"
#menghapus
del(kamus_anime["bluelok"])
print("Kamus terbaru:", kamus_anime)
#PENGECEKAN DATA(KEY)
print("az" in kamus_anime)
#CARA NGECEK ADA KEY AP AJ
print(kamus_anime.keys())
#cara ngecek ad value ap aj
print(kamus_anime.values())
#loopingin
#key
for key in kamus_anime:
    print(key)
#value
for value in kamus_anime.values():
    print(value)
#print key dan value
for key, value in kamus_anime.items():
    print(f"{key} -> {value}")
# BISA MENGGUNAKAN INT JUGA

