def penjumlahan(*myData):
    for i in myData:
        jumlah = sum(i)
    hasil = jumlah
    print('Jumlahnya adalah:', hasil)

def rerata(*myData):
    for i in myData:
        jumlah = sum(i)
        banyak = len(i)
    hasil = jumlah / banyak
    print('Rata-ratanya adalah:', hasil)

def maksimal(*myData):
    for i in myData:
        maks = max(i)
    hasil = maks
    print('Nilai Maksimumnya adalah:', hasil)
    
def minimum(*myData):
    for i in myData:
        minim = min(i)
    hasil = minim
    print('Nilai Minimumnya adalah:', hasil)
