from datetime import*

def diffDate(x):
    skr = datetime.date(datetime.now())
    tgl = x.split('-')
    data = []
    for i in range(len(tgl)):
        data.append(int(tgl[i]))
    y = date(data[0], data[1], data[2])
    hasil = skr - y
    hari = hasil.days
    return hari

file = input('Masukkan file tempat penyimpanan data : ')
myfile = open(file, 'r')
teks = myfile.read().splitlines()
data = []
for i in range(len(teks)):
    x = teks[i].replace('\n', '')
    x = x.split('|')
    data.append(x)
    
kode = input('Masukkan kode member : ')

skr = datetime.date(datetime.now())

print('')
for i in range(len(data)):
    if(kode == data[i][0]):
        status = 'ada'
        selisih = diffDate(data[i][4])
        denda = selisih*2000
        if(selisih <= 0):
            selisih = 0
            denda = 0
        print('Data Peminjaman Buku')
        print('Kode Member		 :', data[i][0])
        print('Nama Member		 :', data[i][1])
        print('Judul Buku		 :', data[i][2])
        print('Tanggal mulai peminjaman :', data[i][3])
        print('Tanggal maks peminjaman  :', data[i][4])
        print('Tanggal pengembalian     :', skr)
        print('Terlambat                :', selisih, 'hari')
        print('Denda                    : Rp', denda)
        break
    else:
        status = 'tidak ada'
if(status == 'tidak ada'):
    print('Data peminjaman buku tidak ada')
myfile.close()
