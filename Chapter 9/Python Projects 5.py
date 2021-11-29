nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("Daftar Nilai Mahasiswa".center(40))
print("========================================")
print("NIM       NAMA         N.MID     N.UAS  ")
print("----------------------------------------")

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(10), end='')
    print(nilai[i]['nama'].ljust(12), end='')
    print(str(nilai[i]['mid']).rjust(6), end='')
    print(str(nilai[i]['uas']).rjust(10))

print("----------------------------------------")

