def listSum( lista=[0, 0, 0 ] ):
    
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + listSum(lista[1:])

list = [1, 2, 3, 4]
print("A soma da lista", list, "é igual a =", listSum(list))