# Mencetak angka terbesar dari ketiga angka yang diinput
def terbesar_dari_tiga():
    # Meminta input angka pertama, kedua dan ketiga
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = int(input("Masukkan angka ketiga: "))
    #Menentukan angka terbesar
    terbesar = max(a, b, c)
    #Menampilkan angka terbesar yang ditemukan
    print("Angka terbesar adalah:", terbesar)

# Memanggil fungsi
terbesar_dari_tiga()