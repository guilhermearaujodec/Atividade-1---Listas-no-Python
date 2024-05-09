"""
Exercício 04Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as idades em outra lista.Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual a 18 anos
"""

lista_idades = []
lista_nomes = []

for i in range(10):
    nome = input('Informe o nome: ')
    lista_nomes.append(nome)
    idade = int(input('Informe a idade: '))
    lista_idades.append(idade)
print(lista_nomes)
print(lista_idades)

print('Pessoas com idade igual ou superior a 18: ')
for indice in range(len(lista_idades)):
    if lista_idades(indice) >= 18:
        print(lista_nomes[indice])