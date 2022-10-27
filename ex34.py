s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    s += n
    if n == 999:
        s -= 999
        cont -= 1
        break
print(f'O total de números digitados foi de {cont} e a soma de todos os valores é de {s}')
