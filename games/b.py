

def b():
    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """

    # write the code solution here

    #Input dari pengguna
    n = input("Masukkan angka-angka yang dipisahkan dengan spasi: ")
    data = [int(x) for x in n.split()]
        
    # Validasi: Data harus memiliki setidaknya dua angka
    if len(data) < 2:
        print("Masukkan setidaknya dua angka.")
        return
        
    # Sorting data
    sorted_data = sorted(data)
    pair = []
    diff = max(sorted_data) - min(sorted_data)
        
    # Mencari pasangan dengan selisih terkecil
    for i in range(len(sorted_data) - 1):
        current_diff = sorted_data[i + 1] - sorted_data[i]
        if current_diff < diff:
            diff = current_diff
            pair = [sorted_data[i], sorted_data[i + 1]]

    # Menampilkan pasangan dengan format sesuai
    print(f"{pair[0]} {pair[1]}")


##Misal
