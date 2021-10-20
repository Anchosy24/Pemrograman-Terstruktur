import random

x = random.randint(0, 100)
print("Main tebak-tebakan yuk!!!")
print("Saya telah memilih bilangan bulat secara acak antara 0 s/d 100... Kamu tebak ya:)")

while True:
    Jawaban = int(input("Tebakan kamu :"))
    if(Jawaban == x):
        print("Selamat!!! Tebakan kamu benar")
        break
    else:
        if(Jawaban > x):
            print("Yah... Tebakan kamu salah nih... Bilangan kamu terlalu besar... Coba lagi yuk!!!")
        elif(Jawaban < x):
            print("Yah... Tebakan kamu salah nih... Bilangan kamu terlalu kecil... Coba lagi yuk!!!")
