print('\033[1;33m{:=^40}\033[m'.format('LOJAS GUANABARA'))
preco = float (input('Qual o valor gasto na loja?'))
print("""FORMAS DE PAGAMENTO
1 - à vista dinheiro/cheque = 10% de desconto.
2 - à vista no cartão = 5% de desconto.
3 - em até 2x no cartão = preço normal.
4 - 3x ou mais no cartão: 20% de juros.""")
pagamento = int(input("Qual será a forma de pagamento?"))
if pagamento == 1:
    novo_preco = preco - (preco * 10 / 100)
    print('O valor a ser pago será de R${:.2f}'.format(novo_preco))
elif pagamento == 2:
    novo_preco = preco - (preco * 5 / 100)
    print('O valor a ser pago será de R${:.2f}'.format(novo_preco))
elif pagamento == 3:
    totparcelas = int(input('Quantas parcelas?'))
    parcela = preco / totparcelas
    print('Sua compra sairá pelo valor normal de {:.2f} dividida em {} parcelas de {:.2f}'.format(preco, totparcelas, parcela))
else:
    novo_preco = preco + (preco * 20 / 100)
    totparcelas = int(input('Quantas parcelas?'))
    parcela = novo_preco / totparcelas
    print('O valor a ser pago será de R${:.2f} dividido em {} parcelas de {}'.format(novo_preco, totparcelas, parcela))