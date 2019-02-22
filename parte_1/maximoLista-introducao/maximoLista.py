def main():
    ''' teste da funcao maximo '''
    teste1 = [1, 5, 8, 9, 0]
    max = max_lista(teste1)
    print("O máximo da lista {} é = {} na posição {}".format(teste1, max[0], max[1]))


def max_lista(lista):
    ''' (list) -> int, int
    recebe uma lista de inteiros e retorna o
    valor maximo da lista e o indice onde ele ocorre '''
    numero = 0
    pos = 0
    for c in range(len(lista)):
        if lista[c] > numero:
            numero = lista[c]
            pos = c

    return numero, pos

main()
