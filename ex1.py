"""
Exercício 01
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e os números ímpares em outra lista.Exiba as duas listas ao usuário.
"""

lista = []
listapares = []
listaimpares = []

for i in range(10):
    numero = int(input('Numero: '))
    lista.append(numero)
    if numero % 2 == 0:
        listapares.append(numero)
    else:
        listaimpares.append(numero)

print(listapares)
print(listaimpares)
