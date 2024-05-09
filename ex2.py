"""
Exercício 02
Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a.A média aritmética dos números armazenados na lista.
b.O somatório dos números pares armazenados na lista.
"""

lista = []
soma = 0
somapares = 0

for n in range(10):
    numero = int(input('Insira um número: '))
    lista.append(numero)
    soma += numero
    if numero % 2 ==0:
        somapares += numero

print(f'{soma / len(lista):.2f}')
print(f'{somapares}')
