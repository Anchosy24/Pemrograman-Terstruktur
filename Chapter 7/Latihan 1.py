try:
    namafile = input("Masukkan nama file :")
    file = open(namafile, "r")
    print("Isi file", namafile, "adalah :")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file tidak ditemukan")
