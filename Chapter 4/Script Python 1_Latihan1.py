print("1. Sebuah rental mobil menyewakan memberikan tarif sewa Rp 200.000 untuk 12 jam pertama, dan untuk berikutnya adalah Rp 10.000/jam. Jika seorang customer menyewa mobil di rental tersebut dari jam 06.00 sampai dengan jam 23.50 (pada hari yang sama), maka tentukan total tarif yang harus dia bayarkan kepada rental mobil!")

#import library
import time

#kasih jeda 3 detik
time.sleep(3)

#Menghitung lama waktu sewa
Awal = 06.00
Akhir = 23.50
print("Awal = 06.00")
print("Akhir = 23.50")
Lama = Akhir - Awal
print("Lama sewa =", "Akhir - Awal =", Akhir, "-", Awal, "=", Lama, "=", round(Lama), "jam")

#kasih jeda 3 detik
time.sleep(3)

#Menghitung tarif sewa
tarif = 200000
print("tarif 12 jam pertama = Rp. 200000")
tarif_tambahan = 10000
print("tarif per jam setelah 12 jam pertama = Rp. 10000")
if Lama == 12 :
   jam_pertama = tarif
   print("Jika, lama sewa 12 jam maka, Tarif sewa = tarif 12 jam pertama")
   print("Tarif sewa = Rp.", jam_pertama)
   print("Jadi, tarif sewa yang harus dibayarkan untuk menyewa mobil selama 12 jam adalah Rp", tarif)
elif Lama > 12 :
    biaya_selanjutnya = tarif + (round(Lama) - 12)*tarif_tambahan
    print("Jika, lama sewa 12 jam maka, Tarif sewa = tarif 12 jam pertama + (Lama - 12) * tarif per jam setelah 12 jam pertama")
    print("Tarif sewa =", tarif, "+", "(", round(Lama), "- 12) *", tarif_tambahan, "= Rp." ,biaya_selanjutnya)
    print("Jadi, tarif sewa yang harus dibayarkan untuk menyewa mobil selama", round(Lama), "jam adalah Rp.", biaya_selanjutnya)

