nome = str(input('Qual é o seu nome?'))
if nome == 'Lorena':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'José':
    print('Seu nome é popular no Brasil.')
elif nome in 'Sophia Enzo Noah':
    print('Seu nome está bem popular no Brasil no momento.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
