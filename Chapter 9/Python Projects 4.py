import random

def shuffleString(x, n):
    daftar = []
    while True:
        if(len(daftar) <= (n-1)):
            string = list(x)
            string = random.sample(string, len(string))
            final = ''.join(string)
            if final in daftar:
                continue
            else:
                daftar.append(final)
        else:
            break
    print(f'randomString({x}, {n}) ->', daftar)

x = str(input('Masukkan teks yang ingin diacak : '))
n = int(input('Masukkan jumlah pengacakan yang diinginkan : '))
shuffleString(x, n)
