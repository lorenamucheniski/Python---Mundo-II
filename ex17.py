print('=' * 50)
print('           10 TERMOS DE UMA PA')
print('=' * 50)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = primeiro + (10 - 1) * razao
for cont in range (primeiro, decimo + razao, razao):
    print('{}'.format(cont), end = ' -> ')
print('ACABOU')