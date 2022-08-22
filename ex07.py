from datetime import date
print('\033[36mCLASSIFICANDO ATLETAS\033[m')
atual = date.today().year
nascimento = int(input('Digite o ano de NASCIMENTO: '))
idade = atual - nascimento
if idade <= 9:
    print('A idade é de {} anos. Até 9 anos a categoria é \033[1;36mMIRIM\033[m!'.format(idade))
elif idade <= 14:
    print('A idade é de {} anos. De 10 à 14 anos a categoria é \033[1;36mINFANTIL\033[m!'.format(idade))
elif idade  <= 19:
    print('A idade é de {} anos. De 15 à 19 anos a categoria é \033[1;36mJÚNIOR\033[m!'.format(idade))
elif idade <= 25:
    print('A idade é de {}. De 20 à 25 anos a categoria é \033[1;36mSÊNIOR\033[m!'.format(idade))
else:
    print('A idade é de {}. Acima de 25 anos a categoria é \033[1;36mMASTER\033[m!'.format(idade))