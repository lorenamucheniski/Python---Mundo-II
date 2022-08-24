print('\033[4;33m=-\033[m' * 20)
print('       \033[33mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[4;33m=-\033[m' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um retângulo!')
    if r1 == r2 == r3:
        print('O retângulo formado será do tipo EQUILÁTERO!')
    elif r1 != r2 != r3:
        print('O retângulo formado será do tipo ESCALENO!')
    else:
        print('O retângulo formado será do tipo ISÓSCELES ')
else:
    print('Os segmentos não podem formar um retângulo!')