buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rerata_semua(Data):
    rerata = int(sum(Data.values()) / len(Data))
    return rerata

print('Daftar buah serta harga satuannya per kg :', buah)
print('Rata-rata harga satuan dari keseluruhan buah yang ada adalah Rp.', rerata_semua(buah))
