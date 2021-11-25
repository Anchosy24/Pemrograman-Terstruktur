#Jumlah memasukkan data
n = int(input('Masukkan jumlah data yang ingin diinput : '))

#input bilangan bulat
i = 1
x = []
while(i <= n):
    bil_bulat = int(input('Masukkan bilangan bulat : '))
    x.append(bil_bulat)
    i = i + 1

#List bilangan bulat
x.sort(reverse=True)
print("Data bilangan bulat dari yang terbesar hingga terkecil :", x)
