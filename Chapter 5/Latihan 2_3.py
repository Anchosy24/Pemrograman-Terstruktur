hitung = 0
jumlah = 0

for x in range(1, 100):
    if(x%2 == 1):
        hitung += 1
        print(x)
        jumlah = jumlah + x
print("")
print("Banyaknya bilangan ganjil :", hitung)
print("Jumlah seluruh bilangan :", jumlah)
