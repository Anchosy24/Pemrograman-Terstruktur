#import library
import time

#masukkan data karyawan
Kode_karyawan = int(input("Masukkan kode karyawan :"))
Nama_karyawan = input("Masukkan nama karyawan :")
Golongan_karyawan = str(input("Masukkan golongan :"))
Status_menikah = input("Masukkan status :")
if(Status_menikah == " 1"):
    Status_menikah = " Menikah"
    Jumlah_anak = int(input("Masukkan jumlah anak :"))
else:
    Status_menikah = " Belum Menikah"

#kasih jeda 3 detik
time.sleep(3)

#menampilkan struktur gaji
if(Golongan_karyawan == " A"):
   Gaji_pokok = 10000000
   if(Status_menikah == " Menikah"):
       Tunjangan_IstriSuami = 10/100*Gaji_pokok
       if(Jumlah_anak > 0):
           Tunjangan_anak = 5/100*Gaji_pokok
   Gaji_kotor = Gaji_pokok + Tunjangan_IstriSuami + Tunjangan_anak
   Potongan = 2.5/100*Gaji_kotor
   Potongan_1 = "2.5%"
   Gaji_bersih = Gaji_kotor - Potongan 
elif(Golongan_karyawan == " B"):
   Gaji_pokok = 8500000
   if(Status_menikah == " Menikah"):
       Tunjangan_IstriSuami = 10/100*Gaji_pokok
       if(Jumlah_anak > 0):
           Tunjangan_anak = 5/100*Gaji_pokok
   Gaji_kotor = Gaji_pokok + Tunjangan_IstriSuami + Tunjangan_anak
   Potongan = 2.0/100*Gaji_kotor
   Potongan_1 = "2.0%"
   Gaji_bersih = Gaji_pokok - Potongan
elif(Golongan_karyawan == " C"):
   Gaji_pokok = 7000000
   if(Status_menikah == " Menikah"):
       Tunjangan_IstriSuami = 10/100*Gaji_pokok
       if(Jumlah_anak > 0):
           Tunjangan_anak = 5/100*Gaji_pokok
   Gaji_kotor = Gaji_pokok + Tunjangan_IstriSuami + Tunjangan_anak
   Potongan = 1.5/100*Gaji_kotor
   Potongan_1 = "1.5%"
   Gaji_bersih = Gaji_pokok - Potongan
elif(Golongan_karyawan == " D"):
   Gaji_pokok = 5500000
   if(Status_menikah == " Menikah"):
       Tunjangan_IstriSuami = 10/100*Gaji_pokok
       if(Jumlah_anak > 0):
           Tunjangan_anak = 5/100*Gaji_pokok
   Gaji_kotor = Gaji_pokok + Tunjangan_IstriSuami + Tunjangan_anak
   Potongan = 1.0/100*Gaji_kotor
   Potongan_1 = "1.0%"
   Gaji_bersih = Gaji_pokok - Potongan
print("====================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------")
print("Nama Karyawan             :", Nama_karyawan, "(kode :", Kode_karyawan, ")")
print("Golongan                  :", Golongan_karyawan)
print("Status Menikah            :", Status_menikah)
if(Status_menikah == " Menikah"):
    print("Jumlah Anak               : ", Jumlah_anak)
print("------------------------------------")
print("Gaji Pokok                : Rp", Gaji_pokok)
print("Tunjangan Istri/Suami     : Rp", Tunjangan_IstriSuami)
print("Tunjangan Anak            : Rp", Tunjangan_anak)
print("------------------------------------+")
print("Gaji Kotor                : Rp", Gaji_kotor)
print("Potongan(", Potongan_1, ")          : Rp", Potongan)
print("-------------------------------------")
print("Gaji bersih               : Rp", Gaji_bersih)
