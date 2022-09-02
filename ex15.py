print('{:-^40}'.format('TABUADA'))
numero = int(input('Digite um número para ver sua tabuada:'))
print('-'*40)
for cont in range (1, 11):
    print('{} X {} = {}'.format(numero, cont, numero*cont))
