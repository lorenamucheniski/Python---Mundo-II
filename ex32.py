soma = cont = maior = menor = 0
continuar = ''
while continuar in 'Ss':
    num = int(input('Digite outro número: '))
    continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = soma / cont
print('__' * 20)
print('A média dos números digitados é de {:.1f}'.format(media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))


