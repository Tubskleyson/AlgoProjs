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