def bintang(n):
     jarak = 2*n-1
     for i in range(n):
          print(('*'*(2*i+1)).center(jarak))


n = int(input("Masukkan bilangan untuk mencetak formasi bintang : "))
bintang(n)
         
     
