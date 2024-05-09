"""
Exercício 05
Preencha a lista com 10 números aleatórios. Na sequência, solicite um número ao usuário e informe quantas vezes esse número aparece na lista.
"""

import random

lista = []
for i in range(10):
    n = random.randint(1, 20)
    lista.append(n)
print(lista)

numero = int(input('Informe um número para procurar na lista: '))

quantidade = lista.count(numero)
print(f'O número {numero} aparece {quantidade} vezes na lista.')

