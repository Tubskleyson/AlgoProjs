from node import Node


class PS:

    def __init__(self, tamanhoMax):

        self.tamanhoMax = tamanhoMax
        self.pilha = [None]
        self.tamanho = 0


    def empilha(self, node):

        if self.tamanho < self.tamanhoMax:

            self.pilha[self.tamanho] = node
            self.pilha.append(None)
            self.tamanho += 1

            return 1

        print('Pilha cheia')
        return


    def desempilha(self):

        if self.tamanho:

            node = self.pilha[self.tamanho-1]
            self.pilha[self.tamanho-1] = None
            del(self.pilha[self.tamanho])
            self.tamanho -= 1

            return node

        print('Pilha vazia')
        return


    def vazia(self):

        return not self.tamanho

    def varrer(self):

        if self.vazia():

            print('Pilha vazia')
            return

        for i in range(self.tamanho): print(self.pilha[i])


class PE:

    def __init__(self):

        self.topo = None


    def inserir(self, node):

        node.anterior = self.topo
        self.topo = node


    def desempilha(self):

        topo = self.topo

        if topo: self.topo = self.topo.anterior

        return topo


    def varrer(self):

        node = self.topo

        while node:

            print(node)
            node = node.anterior


    def vazia(self):

        return not self.topo


    def altura(self, node):

        if not node: return 0
        return 1 + self.altura(node.anterior)


    def profundidade(self, node):

        return self.altura(self.topo) - self.altura(node)

















