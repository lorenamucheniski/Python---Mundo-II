import random as r
print('\033[1;32mPAR OU ÍMPAR\033[m')
print('Vamos jogar PAR ou ÍMPAR!')
cont = 0
while True:
    choice = int(input(f'Digite um valor entre 0 e 10:'))
    computer = r.randint(0,11)
    sum = computer + choice
    player = ' '
    while player not in 'PI':
        player = str(input('PAR OU ÍMPAR? ')).strip().upper()[0]
    print(f'Você jogou o número {choice} e o computador {computer}. Total é de {sum}')
    if player == 'P':
        if sum % 2 == 0:
            print('\033[1;32mVocê venceu!\033[m')
            cont += 1
        else:
            print('\033[1;32mVocê Perdeu!\033[m')
            break
    elif player == 'I':
        if sum % 2 == 1:
            print('\033[1;32mVocê venceu!\033[m')
            cont += 1
        else:
            print('\033[1;32mVocê Perdeu!!\033[m')
            break
