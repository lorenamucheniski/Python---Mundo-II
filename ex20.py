from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range (1, 8):
    nasc = int(input('Em que ano a {}º pessoas nasceu?'.format(pessoas)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade.'.format(totmaior, totmenor))
