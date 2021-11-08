def isPythagoras(a, b, c):
    if(a**2 + b**2 == c**2):
        print('a =', a, 'b =', b, 'c =', c, '-> True')
    else:
        print('a =', a, ',b =', b, ',c =', c, '-> False')

a = int(input('sisi a ='))
b = int(input('sisi b ='))
c = int(input('sisi c ='))
isPythagoras(a, b, c)
