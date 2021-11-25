def kuadrat(bil):
    y = []
    for i in bil:
        bil = i ** 2
        y.append(bil)
    return y

n = int(input('Masukkan jumlah data yang ingin diinput : '))

i = 1
x = []
while(i <= n):
    bil_bulat = int(input('Masukkan bilangan bulat : '))
    x.append(bil_bulat)
    i = i + 1

print('')
print("Data bilangan bulat =", x)
print("Hasil kuadrat dari data tersebut =", kuadrat(x))
