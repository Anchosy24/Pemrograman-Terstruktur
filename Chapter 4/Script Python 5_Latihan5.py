print("5. Buatlah grafik diagram batang horizontal yang merepresentasikan data jumlah anak laki-laki dan perempuan dari mahasiswa PTIK UNS. ")

#import library
import time

#kasih jeda 3 detik
time.sleep(3)

#membuat data statistik jumlah mahasiswa PTIK UNS
print('Grafik jumlah mahasiswa PTIK UNS berdasarkan gender:')
mahasiswa = 41
mahasiswi = 29
print("Jumlah mahasiswa =", mahasiswa)
print("Jumlah mahasiswi =", mahasiswi)
mahasiswa1 = mahasiswa//6
mahasiswi1 = mahasiswi//6
print("_____________Grafik diagram batang horizontal_____________")
print('mahasiswa :',mahasiswa1*'-','(',mahasiswa,')')
print('mahasiswi :',mahasiswi1*'-','(',mahasiswi,')')
