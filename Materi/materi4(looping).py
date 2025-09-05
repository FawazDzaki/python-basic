umur = int(input("masukan umur :"))

if umur >= 18:
    print("kamu usdah dewasa")
else:
    print('kamu masih dibawah umur')    


#project Mingguan

nama = str(input("Siapakah namamu? :"))
umur = int(input('Berapa umur mu? :'))


#project 1/8/25
# index dimuli dari 0 sampai 5
for angka in range(1, 5):
    print("tes", angka)
    print("mantap!")
print('---selesai----')    #ini gak akan masuk kode karna diluar blok kode
 
 #for loop ke string
sandiWifi = "hsiJoglo"
for huruf in sandiWifi: 
 print(huruf, '==>')

#while loop (ulangi sampai kondisi tepenuhi)
no = 1
batas = 10
while(no < batas):
    print(" ulangi ke-", no)
    print("*" * no)
    no += 1

print("--mulai--")
cekUmur = input("berapakah umur anda?")
angkaUmur = int(cekUmur)
if (angkaUmur>=18):
   print('BOLEH BUAT SIM')
else:
   print(" ANDA BELUM CUKUP UMUR!")   
print('--selesai--')
angka = range(3)
for i in angka:
    print("i adalah", i)

for i in range(20):
    print("assalamualaikum ")    
# for in range: untuk mengulang


#tugas 2/8/25
hari2 = ["senin","selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
for i in hari2:
    print(i)