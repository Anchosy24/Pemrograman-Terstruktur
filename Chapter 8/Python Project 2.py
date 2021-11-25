def datastat(x):
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)
    d = [a, b, c]
    return d

n = int(input('Masukkan jumlah data yang ingin diinput : '))

i = 1
x = []
while(i <= n):
    bil_bulat = int(input('Masukkan bilangan bulat : '))
    x.append(bil_bulat)
    i = i + 1

x.sort(reverse=True)
print("Data bilangan bulat :", x)
print("Data stat[rata-rata, nilai maks, nilai min] =", datastat(x))
