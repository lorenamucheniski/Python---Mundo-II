print('\033[1;30;47mGERADOR DE PA\033[m')
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    cont += 1
    termo += razao
print('FIM.')
