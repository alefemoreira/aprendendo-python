def fatorial(n):
    if n==0:
        return 1
    else:
        return n * fatorial(n-1)

def binomial(numerador=1, denomidador=1):

    if denomidador > numerador:
        return "VALORES INVALIDOS, NUMERADOR PRECISA SER MAIOR QUE O DENOMIDADOR"

    return fatorial(numerador) / (fatorial(denomidador) * (fatorial(numerador-denomidador)))

n = int(input("Digite o valor do Numerador fatorial: "))
d = int(input("digite o valor do Denominador fatorial: "))
print("O valor de {} sobre {} é = {}".format(n, d, binomial(n,d)))