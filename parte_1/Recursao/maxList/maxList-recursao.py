def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplo: para a entrada [12, 15, 7], a funcao deve retornar 15.
    '''
# escreva a sua funcao recursiva
    if len(lista) == 1:
        return lista[0]

    if lista[0] > maxR(lista[1:]):
        return lista[0]
    else:
        return maxR(lista[1:])

# escreva os seus testes
lista1 = [12, 15, 7]
print("Teste 1 usando a lista ", lista1, ". Valor maximo encontrado: ",  maxR(lista1))
