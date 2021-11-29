def ubahHuruf(teks, a, b):
    string = teks
    string = string.replace(a, b)
    print(teks ,'->' ,string)

ubahHuruf('MATEMATIKA', 'T', 'S')

teks = str(input('Masukkan teks yang ingin diubah : '))
a = str(input('Masukkan huruf pada teks yang ingin diubah : '))
b = str(input('Masukkan pengganti huruf : '))
ubahHuruf(teks, a, b)
    






