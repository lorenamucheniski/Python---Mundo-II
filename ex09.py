from math import pow
print('\033[4;30;42m     CALCULADORA DE IMC     \033[m')
altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
imc = peso / pow(altura, 2)
print('Seu imc é de {:.1f} - '.format(imc), end= '')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
