file = str(input("Masukkan file yang akan dibuka : "))
myfile = open(file, 'r+')
data = myfile.readlines()
databaru = []
for i in range(len(data)):
    x = data[i].replace('\n', '')
    x = x.split('|')
    databaru.append(x)
    
myfile.seek(0, 0)
teks = myfile.read()
print('Data bilangan yang akan dijumlahkan (bil1|bil2):')
print(teks)
myfile.close()

file = str(input("Masukkan file yang akan ditempati hasil dari file sebelumnya : "))
myfile = open(file, 'a+')

for i in range(len(databaru)):
    bil1 = int(databaru[i][0])
    bil2 = int(databaru[i][1])
    hasil = bil1 + bil2
    myfile.write(f'{hasil}\n')

myfile.seek(0, 0)
teks = myfile.read()
print('Hasil dari penjumlahan data file sebelumnya :')
print(teks)
myfile.close()
