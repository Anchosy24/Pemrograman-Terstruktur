buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def harga_max(Data):
    inverse = [(value, key) for key, value in Data.items()]
    y = (max(inverse)[1])
    return y

print('Daftar buah serta harga satuannya per kg :', buah)
print('Nama buah yang harga satuannya paling mahal adalah', harga_max(buah))
