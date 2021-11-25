buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('-------------------------------')
print('Daftar buah dan harganya      :')
i = 1
for key, values in buah.items():
    print(f'{i}. {key} : Rp. {values}')
    i = i + 1

print('-------------------------------')
print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
while True:
    pilihan = input('Pilihan menu (A/B/C): ')
    if(pilihan == 'A') or (pilihan == 'a'):
        nama = input('Masukkan nama buah    : ')
        if nama in buah:
            print('Nama buah sudah ada dalam dictionary')
            continue
        harga = input('Masukkan harga satuan : ')
        buah[nama] = harga
        print('Database telah diupdate')
        print('-------------------------------')
        print('Daftar buah dan harganya      :')
        i = 1
        for key, values in buah.items():
            print(f'{i}. {key} : Rp. {values}')
            i = i + 1
        continue
    elif(pilihan == 'B') or (pilihan == 'b'):
        print('------------------------------')
        total = []
        while True:
            nama = str(input('Nama buah yang dibeli : '))
            jumlah = int(input('Berapa kg             : '))
            harga_total = (buah.get(nama) * jumlah)
            total.append(harga_total)
            lagi = input('Beli buah yang lain (y/n)? ')
            if(lagi == 'y') or (lagi == 'Y'):
                continue
            elif(lagi == 'n') or (lagi == 'N'):
                break
        total_semua = 0
        for i in total:
            total_semua = total_semua + i
        print('-------------------------------')
        print('Total harga           : Rp.', total_semua)
        break
    elif(pilihan == 'C') or (pilihan == 'c'):
        nama = input('Masukkan nama buah    : ')
        if nama not in buah:
            print('Nama buah tidak ada dalam dictionary')
            continue
        del buah[nama]
        print('Database telah diupdate')
        print('-------------------------------')
        print('Daftar buah dan harganya      :')
        i = 1
        for key, values in buah.items():
            print(f'{i}. {key} : Rp. {values}')
            i = i + 1
        continue
    else:
        print('pilihan tidak valid')
        continue
