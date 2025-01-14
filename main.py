from games.a import a
from games.b import b
from games.c import c


print("""
Welcome to the ODP Games!

Silakan pilih permainan yang ingin Anda mainkan!
(1) Mengubah angka menjadi teks
(2) Mencari pasangan angka dengan selisih terdekat
(3) Mengecek apakah suatu bilangan merupakan bilangan Armstrong

(0) KELUAR
""")

n = input("Pilihan: ")

while n != "0":
    if n == "1":
        a()
    elif n == "2":
        b()
    elif n == "3":
        c()
    else:
        print('Pilihan tidak valid!')
    
    n = input("Pilihan: ")
