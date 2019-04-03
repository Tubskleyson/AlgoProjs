...from filas import *

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(1)
g = Node(2)
h = Node(3)
i = Node(4)
j = Node(5)

f1 = FE()
f2 = FE()
f3 = FE()

f1.inserir(a)
f1.inserir(b)
f1.inserir(c)
f1.inserir(d)
f1.inserir(e)

f2.inserir(Node(2))
f2.inserir(Node(1))
f2.inserir(Node(5))
f2.inserir(Node(3))
f2.inserir(Node(4))

f3.inserir(g)
f3.inserir(f)
f3.inserir(j)
f3.inserir(h)
f3.inserir(i)

l = [f1,f2,f3]

k =1

for i in l:

    print("Teste com a fila",k)

    print('\n\nVarrendo a fila:')
    i.varrer()
    print('\nComprimento da fila por iteração:',i.length_it())
    print('Comprimento da fila por recursão:',i.length_re())
    print('Verifica se a fila está ordenada:',i.ordenada())

    print('\n\n')

    k+=1

print('Altura do node a de f1:', f1.altura(a))
print('Altura do node i de f3:', f3.altura(g))

print('Profundidade do node b de f1:', f1.profundidade(b))
print('Profundidade do node j de f1:', f1.profundidade(j))

print('\n\nf1 e f2 são iguais?', f1.compara_it(f2))
print('f2 e f3 são iguais?', f3.compara_it(f2))

