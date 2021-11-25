sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print("Menu :")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan Data Sayur")

while True:
    pilihan = input('Pilihan anda (A/B/C) : ')
    print('')
    if(pilihan == 'A'):
        print('Anda memilih tambah data sayur')
        sayur.append(input('Masukkan nama sayur yang akan ditambahkan : '))
        continue
    elif(pilihan == 'B'):
        print('Anda memilih hapus data sayur')
        sayur.remove(input('Masukkan nama sayur yang akan dihapus : '))
        continue
    elif(pilihan == 'C'):
        print('Anda memilih tampilkan data sayur')
        print('Daftar sayur :', sayur)
        break
    else:
        print('Pilihan anda tidak valid')
