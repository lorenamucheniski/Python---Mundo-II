print('SEQUÊNCIA DE FIBONACI')
print('~' * 40)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 40)
print('{} -> {} '.format(t1, t2), end= ' ')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print('-> {} '.format(t3), end= ' ')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
