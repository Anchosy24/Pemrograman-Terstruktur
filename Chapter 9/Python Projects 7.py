mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("DATA MAHASISWA".center(61))
print("=============================================================")
print("NIM  	 NAMA MAHASISWA         TGL LAHIR      TEMPAT LAHIR ")
print("-------------------------------------------------------------")

for i in range(len(mhs)):
    mhs[i] = mhs[i].split(':')
    mhs[i][2] = mhs[i][2].split('-')
    mhs[i][2].reverse()
    mhs[i][2] = '/'.join(mhs[i][2])
    print(mhs[i][0].ljust(9), end='')
    print(mhs[i][1].ljust(23), end='')
    print(mhs[i][2].ljust(15), end='')
    print(mhs[i][3].ljust(17))


print("-------------------------------------------------------------")
    
        
        
