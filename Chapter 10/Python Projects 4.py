file = str(input("Masukkan file yang akan dibuka : "))
myfile = open(file, 'r')
teks = myfile.read().splitlines()
data = []
for i in range(len(teks)):
    x = teks[i].replace('\n', '')
    x = x.split('|')
    data.append(x)
    
NIM = input('Masukkan NIM yang mau dicari : ')

print('')
for i in range(len(data)):
    if(NIM == data[i][0]):
        Keterangan = 'Data mahasiswa ditemukan'
        print('Data Mahasiswa')
        print('NIM    :', data[i][0])
        print('Nama   :', data[i][1])
        print('Alamat :', data[i][2])
        break
    else:
        Keterangan = 'Data mahasiswa tidak ditemukan'
        
if(Keterangan == 'Data mahasiswa tidak ditemukan'):
    print(Keterangan)
    
myfile.close()
