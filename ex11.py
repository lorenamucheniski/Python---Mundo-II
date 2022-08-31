from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
print('\033[32m{:#^40}\033[m'.format('PEDRA PAPEL TESOURA'))
print('''Suas opções:
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
jogador = int(input('Qual a sua escolha?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO!!!')
sleep(1)
print('=' * 30)
print('Computador escolheu {}'.format(itens[pc]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('=' * 30)
if pc == 0 and jogador ==2:
    print('Computador venceu!')
elif pc == 1 and jogador == 0:
    print('Computador venceu!')
elif pc == 2 and jogador == 1:
    print('Computador venceu!')
elif pc == jogador:
    print('Jogo empatou!')
else:
    print('Jogador Venceu!')