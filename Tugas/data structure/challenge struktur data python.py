# Tugas/ Tantangan 1 (for loop)
Piket_hari_ini = ['-Syahid', '-Bilal', '-Azka', '-Hanif']
print("jadwal piket hari ini:")
for anggaota_piket in Piket_hari_ini:
   print( anggaota_piket)

print("__________________________________")
# Tugas 2
rukun_islam = ("-Syahadat", "-Solat", "-Zakat", '-Puasa', '-Haji')
print("Rukun islam:")
for rukunIslam in rukun_islam:
   print(rukunIslam)
print("____________________________________")
#tugas 3
kitab_bljr = {"-Kitab ABY", '-Kitab tamhidussabiil', '-Aqidatunaa', '-Nabiyunaa'}
print("Kitab-kitab yang dipelajari:")
for kitab_pelajaran in kitab_bljr:
   print(kitab_pelajaran)

#Rugas 4
biodata_Santri = {
   "nama:": "Dzaki",
    'kelas:': "X-A",
    "Hafalan Juz:": 2}
print("Biodata santri:")
for keys, value in biodata_Santri.items():
   print(keys,value)