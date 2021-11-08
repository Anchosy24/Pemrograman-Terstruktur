from math import floor

def starFormation1(n):
    for n in range(1, n+1):
        for kolom in range(1, n+1):
            print('*', end='')
        print('')
def starFormation2(n):
    for i in range(0, n):
        for j in range(0, n-1):
            print('*', end='')
        n -= 1
        print('')

n = int(input('n ='))
n = floor(n / 2) + 1
starFormation1(n)
starFormation2(n)
