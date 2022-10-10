escolha = 0
print('\033[4;36mOPERAÇÕES\033[m')
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
print('\033[4;36m \033[m' * 30)
while escolha != 5:
    print('\033[1;36mMENU DE OPÇÕES:\033[m')
    print('\033[36m[1]\033[m SOMAR')
    print('\033[36m[2]\033[m MULTIPLICAR')
    print('\033[36m[3]\033[m MAIOR')
    print('\033[36m[4]\033[m NOVOS NÚMEROS')
    print('\033[36m[5]\033[m SAIR DO PROGRAMA')
    escolha = int(input('\033[1;36mComo você deseja continuar?\033[m'))
    if escolha == 1:
        soma = v1 + v2
        print('{} + {} = {}'.format(v1, v2, soma))
        print('\033[4;36m \033[m' * 30)
    elif escolha == 2:
        mult = v1 * v2
        print('{} x {} = {}'.format(v1, v2, mult))
        print('\033[4;36m \033[m' * 30)
    elif escolha == 3:
        if v1 > v2:
            print('{} é maior valor'.format(v1))
        else:
            print('{} é o maior valor'.format(v2))
            print('\033[4;36m \033[m' * 30)
    elif escolha == 4:
        print('Insira novos valores: ')
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
        print('\033[4;36m \033[m' * 30)
    elif escolha == 5:
        print('FIM')
print('PROGRAMA FINALIZADO!')
