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
    hari = abs(hari)
    return hari
    
    
skr = datetime.date(datetime.now())
x = input('Masukkan tanggal (YYYY-MM-DD): ')
selisih = diffDate(x)
print('')
print('selisih hari dari tanggal hari ini', skr, 'dengan tanggal', x, 'adalah', selisih, 'hari')
