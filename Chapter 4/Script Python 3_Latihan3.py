print("3. Berdasarkan informasi dari soal nomor 2, apabila kapasitas tangki bbm mobil pak Budi adalah 50 lt, maka tentukan berapa kali minimal pak Budi harus mengisi bensin hingga penuh supaya bisa menyelesaikan perjalanannya!")

#import library
import time

#kasih jeda 3 detik
time.sleep(3)

#menghitung BBM yang diperlukan selama perjalanan   
Jarak = 795
BBM = 1/12*Jarak
print("Jarak (km)=", Jarak)
print("BBM = 1/12 * Jarak")
print("BBM yang diperlukan = 1/12 *", Jarak, "=", BBM, "lt")

#kasih jeda 3 detik
time.sleep(3)

#menghitung jumlah pengisian BBM yang dilakukan
Tangki = 50
Pengisian = BBM/Tangki
print("Pengisian = BBM/Tangki")
print("Pengisian =", BBM, "/", Tangki, "=", Pengisian)
if Pengisian <= 1 :
    Pengisian_1 = round(Pengisian)
    print("Jika Pengisian <= 1, Jumlah pengisian yang dilakukan = round(Pengisian)")
    print("Jumlah pengisian yang dilakukan =", "round(", Pengisian, ") =", Pengisian_1)
    print("Jadi, agar Pak Budi bisa menyelesaikan perjalanan dengan mobil yang memiliki tangki bensin dengan kapasitas", Tangki, "lt, maka perlu melakukan pengisian bensin minimal", Pengisian_1, "kali")
elif Pengisian > 1 :
    Pengisian_2 = round(Pengisian) + 1
    print("Jika Pengisian > 1, Jumlah pengisian yang dilakukan = round(Pengisian) + 1")
    print("Jumlah pengisian yang dilakukan =", "round(", Pengisian, ") + 1 =" ,Pengisian_2)
    print("Jadi, agar Pak Budi bisa menyelesaikan perjalanan dengan mobil yang memiliki tangki bensin dengan kapasitas", Tangki, "lt, maka perlu melakukan pengisian bensin minimal", Pengisian_2, "kali")

