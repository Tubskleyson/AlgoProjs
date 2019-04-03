from node import Node

class FS:

    def __init__(self,tamanhoMax):

        self.tamanhoMax = tamanhoMax
        self.fila = []
        self.size = 0

    def inserir(self, *args):

        for valor in args:

            if self.size == self.tamanhoMax:

                print("\nFila cheia\n")
                return 1


            self.fila.append(Node(valor))
            self.size += 1

    def acessarNodo(self):

        return self.fila[0].value

    def imprimirFila(self):

        print(*[i.valor for i in self.fila])

    def remover(self):

        self.fila = self.fila[1:]
        self.size -= 1


class FE:

    def __init__(self):

        self.primeiro = None
        self.ultimo = None

    def inserir(self, node):

        if not self.primeiro:

            self.primeiro = node
            self.ultimo = node

        else:

            self.ultimo.prox = node
            self.ultimo = node

    def remover(self):

        if self.primeiro:

            k = self.primeiro.prox

            self.primeiro.prox = None

            self.primeiro = k

    def acessar(self):

        if self.primeiro: return self.primeiro.valor

    def varrer(self):

        node = self.primeiro

        while node:

            print(node,end=' ')
            node = node.prox

        print()

    def length_it(self):

        l = 0

        nde = self.primeiro

        while nde:

            l += 1
            nde = nde.prox

        return l

    def length_re(self):

        return self.lre(self.primeiro)

    def lre(self, nde):

        if not nde: return 0

        return 1 + self.lre(nde.prox)

    def altura(self, nde):

        return self.lre(nde.prx)

    def profundidade(self, nde):

        return self.altura(self.primeiro) - self.altura(nde)

    def ordenada(self):

        if


f = FE()
f.inserir(Node(7))
f.inserir(Node(3))
f.inserir(Node(4))
f.inserir(Node(1))
f.inserir(Node(8))
f.remover()
print(f.length_re())
f.varrer()
