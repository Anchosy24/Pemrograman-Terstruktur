print("4. Pak Amir menempuh perjalanan dari kota A ke B berjarak 125 km dengan rata-rata kecepatan 62 km/jam. Kemudian, dia melanjutkan perjalanan ke kota C berjarak 256 km dari kota B dengan kecepatan rata-rata 70 km/jam. Jika pak Amir berangkat dari kota A pukul 06.00, dan sempat istirahat di kota B selama 45 menit, maka tentukan pukul berapa pak Amir sampai di kota C!")

#import library
import time

#kasih jeda 3 detik
time.sleep(3)

#menghitung jarak kota A ke kota C
print("--------------jarak kota A ke kota C--------------")
Jarak_AB = 125
Jarak_BC = 256
print("Jarak kota A ke kota B (km)=", Jarak_AB)
print("Jarak kota B ke kota C (km)=", Jarak_BC)
Jarak_AC = Jarak_AB + Jarak_BC
print("Jarak antara kota A ke kota C (km)= Jarak kota A ke kota B + Jarak kota B ke kota C =", Jarak_AB, "+", Jarak_BC, "=",Jarak_AC)

#kasih jeda 3 detik
time.sleep(3)

#menghitung laju kecepatan dari kota A ke kota C
print("--------------kecepatan rata-rata dari kota A ke kota C--------------")
Kecepatan_AB = 62
Kecepatan_BC = 70
print("Kecepatan rata-rata dari kota A ke kota B (km/jam)=", Kecepatan_AB)
print("Kecepatan rata-rata dari kota B ke kota C (km/jam)=", Kecepatan_BC)
Kecepatan_AC = Kecepatan_AB + Kecepatan_BC
print("Kecepatan rata-rata dari kota A ke kota C (km/jam)= Kecepatan rata-rata dari kota A ke kota B + Kecepatan rata-rata dari kota B ke kota C =", Kecepatan_AB, "+", Kecepatan_BC, "=", Kecepatan_AC)

#kasih jeda 3 detik
time.sleep(3)

#menghitung lama perjalanan dari kota A ke kota C
print("--------------lama perjalanan dari kota A ke kota C--------------")
Istirahat_B = 45
print("Istirahat di kota B (menit)= ", Istirahat_B)
Lama_perjalanan_AC = Jarak_AC / Kecepatan_AC
print("Lama perjalanan dari kota A ke kota C (jam)= Jarak_AC / Kecepatan_AC =", Jarak_AC, "/", Kecepatan_AC, "=", round(Lama_perjalanan_AC, 2), "jam")
Lama_perjalanan_AC0 = round(Lama_perjalanan_AC*60)
print("Lama perjalanan dari kota A ke kota C (menit) =", Lama_perjalanan_AC0, "menit")
Lama_perjalanan_AC1 = round(Lama_perjalanan_AC*60) + Istirahat_B
print("Lama perjalanan dari kota A ke kota C dengan istirahat (menit)=", round(Lama_perjalanan_AC*60), "+", Istirahat_B, "=", Lama_perjalanan_AC1, "menit")
Lama_perjalanan_AC2 = round(Lama_perjalanan_AC1/60, 1)
print("Lama perjalanan dari kota A ke kota C dengan istirahat (jam)=", Lama_perjalanan_AC2, "jam")
print(Lama_perjalanan_AC2, "jam = 3.36")

#kasih jeda 3 detik
time.sleep(3)

#menentukan waktu tiba di kota C
print("--------------waktu tiba kota C--------------")
Berangkat = 06.00
print("Waktu berangkat =", Berangkat)
Waktu_tiba = Berangkat + 3.36
print("Waktu tiba di kota C =", Berangkat, "+ 3.36 =", Waktu_tiba)
print("Jadi, Pak Amir sampai di kota C pada pukul", Waktu_tiba)

