def starFormation1(n):
    for n in range(1, n+1):
        for kolom in range(1, n+1):
            print('*', end='')
        print('')

n = int(input('n ='))
starFormation1(n)
