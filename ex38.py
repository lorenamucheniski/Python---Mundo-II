print('\033[1;36m    ESTATÍSTICAS EM PRODUTOS\033[m')
counter = sum = less = totmil = 0
while True:
    proceed = cheap = ' '
    print('-' * 30)
    product = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço do produto: R$'))
    counter += 1
    sum += price
    if price > 1000:
        totmil +=1
    if counter == 1 or price < less:
        less = price
        cheap = product
    while proceed not in 'SN':
        proceed = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if proceed == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${sum:.2f}')
print(f'{totmil} produtos custam mais de R$1000,00')
print(f'O produto {cheap} foi o mais barato custando R${less:.2f}')