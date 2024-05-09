"""
Exercício 03
Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
a.a lista com todos os itens armazenados.
b.o somatório de todos os números contidos na lista.
c.o maior número da lista.
d.o menor número da lista.
"""

lista = []
soma = 0

import random

for n in range(20):
    numero = random.randint(1,50)
    lista.append(numero)
    soma += numero

maior_numero = lista[0]
menor_numero = lista[0]

for item in lista:
    if item > maior_numero:
        maior_numero = item

    if item < menor_numero:
        menor_numero = item

print(lista)
print(f'{soma}')
print(f'{maior_numero}')
print(f'{menor_numero}')
