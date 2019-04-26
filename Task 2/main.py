from filas import *
from listas import *

#vamos começar com as listas

lista1 = LE()

#pra facilitar, vamos iniciar a lista com um vetor:

lista1.parse_it([3,1,6,3,2,8])

print("\nMostrando lista geradda por vetor:\n")
lista1.varrer()

print("\nAdcionando 4 ao fim")
lista1.push(Node(4))

print("\nAdcionando 7 ao inicio")
lista1.shift(Node(7))

print("\nResultado:\n")
lista1.varrer()

print("\nA lista tem {} células".format(lista1.count_rec()))
print("\nA lista está em ordem crescente?")
print(lista1.ord())
print("\nO menor item da lista é o",lista1.min_it())
print("\nO {} é o item mais no meio da lista".format(lista1.mid()))

lista2 = lista1.clone_rec()
print("\nLista 2 gerada como clone da lista 1:\n")
lista2.varrer()
print("\nPodemos aleterar a lista 2 sem modificar a lista 1")
print("\nNa lista 2, vamos trocar o primeiro e o ultimo item de posição:")
lista2.switch(0,lista2.count_it()-1)
print("\nResultado:\n")
lista2.varrer()

print("\nE a lista 1 permanece a mesma:\n")
lista1.varrer()
