#kalkulator sederhana penghitung kembalian

#input
makanan= int(input("Harga makanan sebesar Rp ", ))
snack= int(input("Harga minuman sebesar Rp ", ))
minuman= int(input("Harga minuman sebesar Rp ", ))
uang= int(input("Uang yang anda bawa sebsar Rp ", ))

#proses
total= makanan+snack+minuman
if total>uang:
    print("Total yang harus anda bayar sebesar Rp", total)
    print("Uang Anda Kurang! Anda memiliki utang sebesar Rp",(total-uang))
elif total==uang:
    print("Total yang harus anda bayar sebesar Rp", total)
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
else:
    print("Total yang harus anda bayar sebesar Rp", total)
    print("Anda memiliki kembalian sebesar Rp",(uang-total))


