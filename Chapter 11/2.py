from datetime import*

file = input('Masukkan file tempat penyimpanan data : ')
myfile = open(file, 'a+')

skr = datetime.date(datetime.now())
kembali = skr + timedelta(days = 7)
while True:
    kode = input('Masukkan kode member : ')
    nama = input('Masukkan nama member : ')
    buku = input('Masukkan judul buku  : ')
    myfile.write(f'{kode}|{nama}|{buku}|{skr}|{kembali}\n')
    tambah = input('input data lagi (y/n): ')
    if(tambah == 'y') or (tambah == 'Y'):
        continue
    else:
        break

myfile.seek(0, 0)
data = myfile.read()
print('')
print('Data Peminjaman Buku')
print(data)
myfile.close()
