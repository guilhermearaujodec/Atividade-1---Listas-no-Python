"""
Exercício 06
Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma nota menor que zero). Após a entrada de dados, exiba:
a.A quantidade de notas que foram informadas.
b.Todas as notas na ordem em que foram informadas.
c.A média aritmética de todas as notas.
d.A quantidade de notas acima da média aritmética calculada.
"""

lista = []

while True:
    notas = int(input('Informe uma nota: '))
    if notas < 0:
        break
    lista.append(notas)
    
print('Quantidade de notas: {len(lista)}')      # A quantidade de notas que foram informadas.
print(lista)                                    # Todas as notas na ordem em que foram informadas.

media = sum(lista) / len(lista)                 # A média aritmética de todas as notas.
print(f'Média: {media:.2f}')

cont = 0                                        # A quantidade de notas acima da média aritmética calculada.
for item in lista:
    if item > media:
        cont += 1

print(f'Quantidade de notas acima da média: {cont}')
