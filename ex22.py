somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehove = ' '
totmulheres = 0

for p in range (1,5):
    print('------ {}º PESSOA ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehove = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        nomehove = nome
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(maioridadehomem, nomehove))
print('{} mulheres tem menos de 20 anos de idade.'.format(totmulheres))
