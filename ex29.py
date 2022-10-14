print('\033[1;32mGERADOR DE PA\033[m')
primeiro = int(input('\033[1mPrimeiro termo: \033[m'))
razao = int(input('\033[1mRazão da PA: \033[m'))
termo = primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end = ' ')
        cont += 1
        termo += razao
    print('\033[31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('\nProgressão finalizada com {} termos mostrados.'.format(total))



