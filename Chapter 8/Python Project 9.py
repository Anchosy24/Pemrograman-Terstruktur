buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('------------------------------')
print('Daftar buah dan harganya     :')
i = 1
for key, values in buah.items():
    print(f'{i}. {key} : {values}')
    i = i + 1

print('------------------------------')
nama = str(input('Nama buah yang dibeli : '))
jumlah = int(input('Berapa kg             : '))
harga_total = buah.get(nama) * jumlah
print('------------------------------')
print('Total harga           : Rp.', harga_total)
 
