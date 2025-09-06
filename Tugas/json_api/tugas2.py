import requests
url = f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
response = requests.get(url) # Http Get (ambil data)
data_json = response.json()

nama_surah = data_json["data"]
print(f"Ayat Al-Kursi (2:225) -Arab : {nama_surah["text"]}")


import requests
url = f"https://api.alquran.cloud/v1/ayah/2:255/en.asad"
response = requests.get(url) 
data_json = response.json()

nama_surah = data_json["data"]
print(f"Terjemahan (EN) : {nama_surah["text"]}")