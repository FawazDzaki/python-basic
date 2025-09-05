print( 'MATERI 8 - FUNCTION BASIC')
print("_______________________________")
 # function diawali dengan keyword 'def
def halo_ngab():
      print("Halo ngab")
      print("Halo juga bang")
      print("____________________")
halo_ngab()# cara manggil nya gak perlu pke print lagi 
  #function dengan parameter 'nama'
def sapa_sapa(nama):
      print("halo bro",nama)
      print("apa kabare bang",nama)
      print("___________")
sapa_sapa("wildan")
sapa_sapa("thufail")
sapa_sapa("zidan")
sapa_sapa("azka")

  #fungsi luas persegi panjang:
def luas_persegi_panjang(panjang, lebar):
      print("> panjang:", panjang)
      print("> lebar:", lebar)
      rumus = panjang * lebar
      print("luas persegi panjang = ", rumus)
luas_persegi_panjang(20, 30)
luas_persegi_panjang(2000, 100)

#project
def luas_jajar_genjang(alas, tinggi):
      print("alas:", alas)
      print("tinggi:", tinggi)
      rumus = alas * tinggi
      print("luas_jajar_genjang =", rumus)
luas_jajar_genjang(40, 50)

def luas_segitiga( alas, tinggi):
      print("alas:", alas)
      print("tinggi:", tinggi)
      rumus = 1/2  * alas * tinggi
      print("luas segitiga =", rumus)
      luas_segitiga(30, 28)

def luas_layang_layang(d1, d2):
      print("diagonal 1 =", d1)
      print("diagonal 2 =", d2)
      rumus = 1/2 * d1 * d2
      print("luas layang layang =", rumus)
luas_layang_layang(10, 30)




#_____________________________MAS HAMKA____________________________________
# function biasa
def sapa():
     return "assalamualaikum" # kalau return print("assalamulikum")

print(sapa())# disini langsung sapa

# dengan parameter
def sapaNama1(nama):
     return print(f"assalamualaikum {nama}")

sapaNama1("ucok")

def sapaNama2(nama, umur):
     return print(f"assalamualaikum", nama, "umur kamu", umur)

sapaNama2("ucok", 20)


  