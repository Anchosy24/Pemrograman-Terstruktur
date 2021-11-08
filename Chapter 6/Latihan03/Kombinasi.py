from faktorial import *

def Permutasi(a, b):
    hasil = faktorial(a) / faktorial(a-b)
    return hasil

print('b. P(10, 7)')
print('Jawab :')
a = 10
b = 7
print('P(', a, ',', b, ') =', a, '! / (', a, '-', b, ') ! =', Permutasi(a, b))
