import sys

#masukkan nama file tujuan
namafile = input("Masukkan nama file yang dibutuhkan : ")

#Menampilkan isi file
try:
    file = open(namafile, "r")
    print("Isi file", namafile, "adalah :")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file tidak ditemukan")
    sys.exit()

#Menambahkan isi file
file = open(namafile, "a")
xxx = input("Data yang mau ditambahkan :")
file.write(xxx)
while True:
    yn = input("Mau lagi (y/n) : ")
    if(yn == 'y'):
        xxx = input("Data yang mau ditambahkan :")
        file.write(xxx)
        continue
    elif(yn == 'n'):
        file.close()
        break
    else:
        print("Maaf pilihan anda tidak valid")
        continue
