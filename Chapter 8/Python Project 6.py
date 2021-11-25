def sortStringByChar(myData):
    myData.sort(reverse = True, key = len)
    return myData

n = int(input('Masukkan jumlah data yang ingin diinput : '))

i = 1
x = []
while(i <= n):
    buah = str(input('Masukkan nama buah : '))
    x.append(buah)
    i = i + 1

print('')
print('Daftar buah =', x)
print('Hasil susunan urutan buah =', sortStringByChar(x))
