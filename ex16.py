soma = 0
c = 0
for cont in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        c += 1
print('Você informou {} números PARES e a soma desses números é igual a: {}'.format(c, soma))

