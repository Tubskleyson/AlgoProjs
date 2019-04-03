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

        node = self.primeiro

        while node:

            l += 1
            node = node.prox

        return l

    def length_re(self):

        return self.lre(self.primeiro)

    def lre(self, node):

        if not node: return 0

        return 1 + self.lre(node.prox)

    def altura(self, node):

        return self.lre(node.prox)

    def profundidade(self, node):

        return self.altura(self.primeiro) - self.altura(node)

    def ordenada(self):

        ord = 1

        node = self.primeiro

        while node.prox:

            ord *= node.valor < node.prox.valor
            node = node.prox

        return bool(ord)


    def compara_it(self, fila):

        if self.length_it() != fila.length_it(): return False

        n1 = self.primeiro
        n2 = fila.primeiro

        iguais = 1

        while n1 and n2:

            iguais *= n1.valor == n2.valor
            n1 = n1.prox
            n2 = n2.prox

        return bool(iguais)

    def compara_re(self, fila):

        if self.length_it() != fila.length_it(): return False

        return bool(self.cre(self.primeiro, fila.primeiro))

    def cre(self, n1, n2):

        if not n1: return 1
        return n1.valor==n2.valor * self.cre(n1.prox, n2.prox)


