from Node import Node

class FilaSequencial:

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