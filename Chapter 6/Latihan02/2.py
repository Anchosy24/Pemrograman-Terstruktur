def starFormation2(n):
    for i in range(0, n):
        for j in range(0, n):
            print('*', end='')
        n -= 1
        print('')
                
n = int(input('n ='))
starFormation2(n)
