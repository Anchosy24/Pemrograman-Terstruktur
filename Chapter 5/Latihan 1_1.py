#import library
import time

#Masukkan input nilai
Nilai_Indonesia = int(input("Masukkan nilai Bahasa Indonesia :"))
Nilai_IPA = int(input("Masukkan nilai IPA :"))
Nilai_Matematika = int(input("Masukkan nilai Matematika :"))
print('')

#kasih jeda 3 detik
time.sleep(3)

#menunjukkan data
print("-----------Status Kelulusan-----------")
print("Nilai Bahasa Indonesia =", Nilai_Indonesia)
print("Nilai IPA =", Nilai_IPA)
print("Nilai Matematika =", Nilai_Matematika)
print('')

#menunjukkan status kelulusan
if(Nilai_Indonesia >= 60) and (Nilai_IPA >= 60) and (Nilai_Matematika > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
