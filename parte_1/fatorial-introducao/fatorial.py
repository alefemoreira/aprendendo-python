'''
capítulo: introdução
autor: Alefe de Lima Moreira
programa: Fatorial
'''

def main():
    '''FUNÇÃO PRINCIPAL'''
    n = int(input("Digite um número POSITIVO E INTEIRO para saber o seu fatorial: "))
    if n >= 0:
        f = fatorial(n)
        print('O fatorial do numero que vc digitou é: \033[0;31m {} \033[m'.format(f))
    else:
        print('NUMERO INVÁLIDO')

#---------------------------------------------------------------------------------------

def fatorial(numero):
    ''' (int) -> int
    Recebe um inteiro numero e retorna o valor do fatorial
    de numero.
    '''

    fatorial = 1

    if numero == 0 or numero == 1:
        return 1

    while numero > 0:
        fatorial *= numero
        numero -= 1

    return fatorial 

#INICIA O PROGRAMA
main()