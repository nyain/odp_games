def c():
    """
    Periksa apakah sebuah angka merupakan bilangan Armstrong.

    Keluaran:
    None: Cetak hasil apakah angka adalah bilangan Armstrong atau bukan.
    """
    # Ambil input dari pengguna
    num = int(input("Enter a number: "))

    # Hitung jumlah digit
    num_digits = len(str(num))

    # Inisialisasi sum
    total = 0

    # Menjumlahkan setiap digit yang dipangkatkan sesuai jumlah digit
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits  # Angka dipangkatkan sesuai jumlah digit
        temp //= 10  # Menghapus digit terakhir

    # Menampilkan hasil
    if num == total:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
