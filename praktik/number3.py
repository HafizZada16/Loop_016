#Mencetak deret fibonacci hingga angka sesuai input
def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a < n:
        hasil.append(a)
        a, b = b, a + b
    return hasil

# Memanggil fungsi dengan input dari pengguna
n = int(input("Masukkan batas n untuk seri Fibonacci: "))
print("Seri Fibonacci hingga", n, "adalah:", fibonacci(n))
