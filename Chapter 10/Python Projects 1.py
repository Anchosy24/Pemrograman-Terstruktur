file = str(input("Masukkan file yang akan dibuka : "))

myFile = open(file, 'r')
note = myFile.read()
print('Data dalam file :')
print(note)
myFile.close()

myFile = open(file, 'r')
list_note = myFile.readlines()
genap = []
ganjil = []
for i in range(len(list_note)):
    if(i%2 == 0):
        genap.append(list_note[i])
    if(i%2 == 1):
        ganjil.append(list_note[i])

print("Banyaknya bilangan genap dalam data file =", len(genap))
print("Banyaknya bilangan ganjil dalam data file =", len(ganjil))
myFile.close()
