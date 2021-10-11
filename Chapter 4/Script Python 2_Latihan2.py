print("2. Pak Budi melakukan perjalanan dari kota A menuju kota C yang berjarak 795 km menggunakan sebuah mobil via jalan tol. Apabila konsumsi bbm mobil pak Budi adalah 1:12 (1 lt bbm dapat digunakan untuk menempuh 12 km), maka berapa liter bensin yang diperlukan untuk perjalanan tersebut?")

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
print("Jadi, BBM yang diperlukan selama perjalanan dengan jarak", Jarak, "km adalah", BBM, "lt")
