soma = 0
cont = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a sua soma é de {}.'.format(cont, soma))
