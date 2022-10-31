cont = 0 
while True:
    n = int(input('\033[1;36mDigite um número para ver sua tabuada: \033[m'))
    print('\033[36m-\033[m' * 35)
    if n < 0 :
        print('Número Invalido... Programa finalizado!')
        break
    for cont in range (0,10):
        cont += 1
        print(f'\033[1m{n} x {cont}\033[m = {n*cont}')
    print('\033[36m-\033[m' * 40)


