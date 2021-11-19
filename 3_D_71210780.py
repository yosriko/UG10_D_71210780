#daftar belanjaan


db = input("Masukkan daftar belanja Anda : ")
dbs= db.split()
dbsc= [i.capitalize() for i in dbs]
print("Daftar belanja:", dbsc)

tambah = input("Masukkan barang yang ingin ditambahkan: ")

if tambah in dbsc:
    print("Barang", tambah.upper(), "sudah berada dalam daftar belanja.")
    


