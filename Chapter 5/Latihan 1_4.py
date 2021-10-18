#import library
import time

#masukkan data karyawan
Kode_karyawan = int(input("Masukkan kode karyawan :"))
Nama_karyawan = input("Masukkan nama karyawan :")
Golongan_karyawan = str(input("Masukkan golongan :"))
Status_menikah = input("Masukkan status(1:menikah, 2:blm):")
if(Status_menikah == " 1"):
    Status_menikah = "Menikah"
    Jumlah_anak = input("Masukkan jumlah anak :")
else:
    Status_menikah = "Belum Menikah"

#kasih jeda 3 detik
time.sleep(3)

#menampilkan struktur gaji
if(Golongan_karyawan == " A"):
   Gaji_pokok = 10000000
   Potongan = 2.5/100*Gaji_pokok
   Potongan_1 = "2.5%"
   Gaji_bersih = Gaji_pokok - Potongan 
elif(Golongan_karyawan == " B"):
   Gaji_pokok = 8500000
   Potongan = 2.0/100*Gaji_pokok
   Potongan_1 = "2.0%"
   Gaji_bersih = Gaji_pokok - Potongan
elif(Golongan_karyawan == " C"):
   Gaji_pokok = 7000000
   Potongan = 1.5/100*Gaji_pokok
   Potongan_1 = "1.5%"
   Gaji_bersih = Gaji_pokok - Potongan
elif(Golongan_karyawan == " D"):
   Gaji_pokok = 5500000
   Potongan = 1.0/100*Gaji_pokok
   Potongan_1 = "1.0%"
   Gaji_bersih = Gaji_pokok - Potongan
print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------")
print("Nama Karyawan             :", Nama_karyawan, "(kode :", Kode_karyawan, ")")
print("Golongan                  :", Golongan_karyawan)
print("------------------------------------")
print("Gaji pokok                : Rp", Gaji_pokok)
print("Potongan(", Potongan_1, ")          : Rp", Potongan)
print("-------------------------------------")
print("Gaji bersih               : Rp", Gaji_bersih)

