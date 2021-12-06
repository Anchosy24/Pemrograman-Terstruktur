file = str(input("Masukkan file yang akan dibuka : "))
myfile = open(file, 'r')
teks = myfile.readlines()
data = []
for i in range(len(teks)):
    x = teks[i].replace('\n', '')
    x = x.split('|')

    y = {'NIM' : x[0], 'Nama' : x[1], 'Alamat' : x[2] }
    data.append(y)
    
print('')
print('Data Mahasiswa =', data)
myfile.close()
