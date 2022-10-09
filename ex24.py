from random import randrange
from time import sleep
c = 1
computer = randrange(0, 10)
print('Sou seu computador! Pensarei em um número entre 0 e 10 .... Tente adivinhar!')
sleep(5)
print('3')
sleep(1)
print('2')
sleep(1)
print('1 .... ')
sleep(1)
jogador = int(input('Em qual número eu pensei? '))
while jogador != computer:
    jogador = int(input('Você errou! Tente novamente! Em qual número eu pensei? '))
    c += 1
print('=-' * 35)
print('VOCÊ ACERTOU! Foram precisos {} palpites para vencer!'.format(c))
