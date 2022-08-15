print('==' * 20)
print('         EMPRÉSTIMO BANCÁRIO')
print('==' * 20)
valor = float(input('Qual o valor da casa que você deseja comprar?'))
salario = float(input('Qual é o seu salário?'))
anos = float(input('Em quantos anos você pagará a casa?'))
prestacao = valor / (anos*12)
if prestacao > salario * 30 / 100:
    print('O valor da prestação é maior que 30% do seu salário. Infelizmente seu empréstimo foi negado!')
else:
    print('PARABÉNS! Seu empréstimo foi aprovado!')
print('O valor da prestação será de R${:.2f}'.format(prestacao))