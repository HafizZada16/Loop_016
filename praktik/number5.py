def segitiga_angka():
    n = int(input("Masukkan nilai n untuk segitiga angka: "))
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)

# Memanggil fungsi
segitiga_angka()