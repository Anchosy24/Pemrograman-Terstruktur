buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('-------------------------------')
print('Daftar buah dan harganya      :')
i = 1
for key, values in buah.items():
    print(f'{i}. {key} : {values}')
    i = i + 1

print('------------------------------')
total = []
while True:
    nama = str(input('Nama buah yang dibeli : '))
    jumlah = int(input('Berapa kg             : '))
    harga_total = buah.get(nama) * jumlah
    total.append(harga_total)
    lagi = input('Beli buah yang lain (y/n)? ')
    if(lagi == 'y') or (lagi == 'Y'):
        continue
    elif(lagi == 'n') or (lagi == 'N'):
        break
total_semua = sum(total)
print('-------------------------------')
print('Total harga           : Rp.', total_semua)
 
