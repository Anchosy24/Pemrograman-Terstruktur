a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

a.insert(3, 10)
b.insert(2, 15)

a.append(4)
b.append(8)

a.sort()
b.sort()
print('a =', a)
print('b =', b)

c = list(a[0:8])
d = list(b[2:10])
print('c =', c)
print('d =', d)

for x in c and d:
    i = 0
    e = []
    while(i <= 7):
        x = (c[i] + d[i])
        e.append(x)
        i = i + 1

print('e =', tuple(e))
print('Nilai minimum dari elemen e =', min(e))
print('Nilai maksimum dari elemen e =', max(e))
print('Nilai jumlah seluruh elemen e =', sum(e))


