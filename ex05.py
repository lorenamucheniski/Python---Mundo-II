from datetime import date
atual = date.today().year
print('\033[4:32mALISTAMENTO MILITAR\033[m')
nascimento = int(input('Informe o ano do seu nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos de idade.'.format(nascimento,idade))
if idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para você completar 18.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você deveria ter se alistado à {} anos atrás, em {}.'.format(saldo, alistamento))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')

