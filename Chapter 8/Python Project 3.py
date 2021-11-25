n = int(input('Masukkan jumlah data yang ingin diinput : '))

i = 1
x = []
while(i <= n):
    mahasiswa = str(input('Masukkan nama Mahasiswa : '))
    x.append(mahasiswa)
    i = i + 1

x.sort()
print('')
print("Daftar Mahasiswa :")

for mahasiswa in x:
    jumlah = len(mahasiswa)
    print(mahasiswa, f'({jumlah} karakter)')
