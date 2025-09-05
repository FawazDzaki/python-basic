import json
# tambah kan module "json" dengan import
print("____MATERI 12 - JSON HANDLING_________")
print("_________________READ JSON_____________")
file_path =  r"C:\Users\User\Desktop\Project IT\materi-kelas-a\materi.json"
# with open untuk otomatis ke close
with open(file_path, 'r') as file_materi:
  # json.load() --> membaca isi file pesan
  data_materi = json.load(file_materi)
  # keys: "title", "total", "Status_Santri", "Status_lulus"
  #akses data json dengan key nya
  print(f"JUDUL BERKAS:{data_materi["title"]}")
  print(f"TOTAL KELAS A:{data_materi["total"]}")
  print(f"Status santri:{data_materi["Status_Santri"]}")
  print(f"Status kelulusan:{data_materi["Status_lulus"]}")
  # ekstrak data list (palajaran) dgn for loop
  for pelajaran in data_materi["Pelajaran"]:
    print(f"-->{pelajaran}")
  # esktrak semuadata array of object surah
  # di python diebut juga list of dictionary
  # keys surah: "no", "nama", "ayat", "turun"
  print("-"*50)# gandakan sibol gengan perkalian
  print("|no|Nama surah|ayat|Tempat turun|")
  print("_"*50)
  for surah in data_materi["Surah"]:
    print(f"|{surah["no"]} | {surah["Nama"]} | {surah["ayat"]} | {surah["turun"]} ")



