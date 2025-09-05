# print("MATERI 9") 
# print("_____________")
def say_hello(nama):
     #print("halo mr., name") ----> versi dengan koma
     #kasih f di depan string untuk penggabungan
     print(f'hello Mr.{nama}')
     print("baek baek aee")

# Lambda untuk menulis fungsi yang ringkas dengan 1 baris saja
 # Sering disebut juga funsi yang anonim (tanpa nama)
# struktur lambda: [lambda] [parameter] [isinya]
say_hello_mini = lambda name: print(f'hello mr.{name}')
# pnggil fungsi2nya dibawah ini
say_hello("azzam")
say_hello("udin")
# print("_________________")
say_hello_mini("syahid")
say_hello_mini("thufail")

# contoh penerapan lambda dengan higher-order function
# map()---sorted()-----filter()
jajan_mingguan = [
    50000, 
    7000, 
    40000,
    2000,
    150000
]
urutan_Uang =  sorted(jajan_mingguan)
print(urutan_Uang)

urutanUangTerbalik = sorted(jajan_mingguan, reverse=True)
print(f"urutan uang:{urutan_Uang}")
print(f"urutan uang terbalik:{urutanUangTerbalik}")

# map()--> mentranformasikan data
kurangin_uang = map(lambda uang : uang - 5000,jajan_mingguan)
#list() mengubah data objek map menjadi bentuk list
list_kurangin_uang = list(kurangin_uang)
print(f"map uang berkurang: {list_kurangin_uang}")

# filter() menyaring / memfilter data
jajan_banyak = filter(lambda uang: uang > 40000,jajan_mingguan)
list_jajan_banyak = list(jajan_banyak)
print(f"filter jajan diatas 30rb:{list_jajan_banyak}")
