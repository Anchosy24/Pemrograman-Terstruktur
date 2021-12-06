file = str(input("Masukkan file yang akan ditambahkan data : "))
myfile = open(file, 'a+')

while True:
    NIM = input('Masukkan NIM            : ')
    Nama = input('Masukkan Nama Mahasiswa : ')
    Alamat = input('Masukkan Alamat         : ')
    myfile.write(f'{NIM}|{Nama}|{Alamat}\n')
    Ulang = input('Tambah data lagi (y/n)  : ')
    print('')
    if(Ulang == 'Y' or Ulang == 'y'):
        continue
    elif(Ulang == 'N' or Ulang == 'n'):
        break

myfile.seek(0, 0)
teks = myfile.read()
print('Data dalam file :')
print(teks)
myfile.close()
