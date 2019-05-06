class Node:

    def __init__(self, valor):

        self.valor = valor
        self.prox = None
        self.ant = None




    def __repr__(self):

        return 'Node de valor '+str(self.valor)
