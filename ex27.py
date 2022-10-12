print('\033[1;4mFATORIAL\033[m')
num = int(input('Digite um número para ver seu fatorial: '))
f = 1
print('Calculando {}! = '.format(num), end = ' ')
for cont in range(num , 0 , -1):
    print('{}'.format(cont), end = ' ')
    print('x' if cont > 1 else '=', end = ' ')
    f*= cont
print('{}'.format(f))

