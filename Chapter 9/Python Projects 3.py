def bintang(n):
     jarak = n + 2
     x = int(n/2+0.5)
     y = int(n/2-0.5)
     for i in range(x):
          print(('*'*(2*i+1)).center(jarak))
     for j in reversed(range(y)):
          print(('*'*(2*j+1)).center(jarak))


n = int(input("Masukkan bilangan ganjil untuk mencetak formasi bintang : "))
bintang(n)
