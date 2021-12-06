file = str(input("Masukkan file teks sandi : "))
myfile = open(file, 'r')
teks = myfile.read()
print('Teks sandi'.center(len(teks)))
print(teks)
teks = list(teks)

print('')
n = int(input('Masukkan nilai pergeseran sandi : '))
data = []
for i in range(len(teks)):
    a = ord(teks[i])
    keyword = a - n
    if(a == 32):
        asli = chr(32)
    elif(keyword < 65):
        asli = chr(91-(65-keyword))
    else:
        asli = chr(keyword)
    data.append(asli)
        
baru = ''.join(data)
myfile.close()

print('')
file = str(input("Masukkan file untuk penempatan teks asli : "))
myfile = open(file, 'a+')

myfile.write(baru)
myfile.seek(0, 0)
teks = myfile.read()
print('Teks asli'.center(len(teks)))
print(teks)
