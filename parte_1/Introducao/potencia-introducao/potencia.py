def main():
    '''FUNÇÃO PRINCIPAL'''

    base = float(input('digite um numero real: '))
    expoente = int(input('digite uma potencia para elevar o numero anterior: '))

    pot = potencia(base, expoente)

    print('\033[0;31m{}\033[m elevado a \033[0;32m{}\033[m é = \033[0;33m{}\033[m'.format(base, expoente, pot))

def potencia(base, expoente):
    '''Recebe uma base -> Float
    Recebe um expoente -> Inteiro
    e imprime a o valor da potencia'''
    potencia = 1

    for c in range(0, expoente):
        potencia *= base

    return potencia

main()
