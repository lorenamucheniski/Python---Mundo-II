soma = 0
cont = 0
print('{:=^35}'.format('SOMA DOS MÚLTIPLOS DE 3'))
print('A soma será feita entre um intervalo de números de 1 a 500...')
print('-=' * 30)
for n in range (1, 501):
    if n % 3 == 0:
        cont +=1
        soma += n
print('''Entre 1 e 500 existem {} números que são múltiplos de 3.
A soma de todos esses números é igual a {}.'''.format(cont, soma))


