print('\033[1;31;40m     MÉDIA      \033[m ')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5.0:
    print('\033[1;31mREPROVADO!\033[m')
elif media > 5.0 and media < 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
elif media > 7.0:
    print('\033[1;32mAPROVADO!\033[m')
print('As notas foram {} e {}, dando uma média de {:.1f}!'.format(n1, n2, media))
