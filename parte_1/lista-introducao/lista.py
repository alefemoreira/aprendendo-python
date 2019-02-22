seq = list()
n = int(input('Digite o tamanho da lista: '))

for c in range(n):
    num = int(input('Digite um valor inteiro para o {}° elemento: '.format(c+1)))
    seq.append(num)

print('Lista digitada: ', end=" ")
print(seq)

print('Lista invertida:', end=" ")
for c in range(n-1, -1, -1):
    print(seq[c], end=" ")

print()
