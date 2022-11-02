print('\033[1;35mCADASTRO DE PESSOAS\033[m')
larger = man = woman = 0
while True:
    sex = proceed = ' '
    print('.' * 20)
    age = int(input('Digite a idade: '))
    while sex not in 'MF':
        sex = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while proceed not in 'SN':
        proceed = str(input('Deseja continuar ? [S/N] : ')).strip().upper()[0]
    if proceed == 'N':
        break
    elif sex == 'M':
        man += 1
    elif age >= 18:
        larger += 1
    elif sex == 'F':
        if age <= 20:
            woman += 1
print('.' * 26)
print('\033[1;31mCadastro Encerrado!\033[m')
print(f'{larger} pessoas tem mais de 18 anos.')
print(f'{man} homens foram cadastrados.')
print(f'{woman} mulheres com menos de 20 anos foram cadastradas.')
