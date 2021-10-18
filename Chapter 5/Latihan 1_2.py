#import library
import time

#Masukkan input nilai
Nilai_Indonesia = int(input("Masukkan nilai Bahasa Indonesia :"))
Nilai_IPA = int(input("Masukkan nilai IPA :"))
Nilai_Matematika = int(input("Masukkan nilai Matematika :"))

#kasih jeda 3 detik
time.sleep(3)

#menunjukkan status kelulusan
print("-----------Status Kelulusan-----------")
print("Nilai Bahasa Indonesia =", Nilai_Indonesia)
print("Nilai IPA =", Nilai_IPA)
print("Nilai Matematika =", Nilai_Matematika)

if(Nilai_Indonesia > 100) or (Nilai_Indonesia < 0) or (Nilai_IPA > 100) or (Nilai_IPA < 0) or (Nilai_Matematika < 0) or (Nilai_Matematika > 100):
    print("Maaf input ada yang tidak valid")
elif(Nilai_Indonesia >= 60) and (Nilai_IPA >= 60) and (Nilai_Matematika > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
