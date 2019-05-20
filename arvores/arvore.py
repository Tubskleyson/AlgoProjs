from node import Node


class Arvore:

    def __init__(self):

        self.raiz = None
    
    
    def inserir_raiz(self, raiz):

        if not self.raiz: 
            self.raiz = Node(raiz)
            return 1

        return 0

    def inserir(self, valor, pai):

        pai = self.acessar(pai)

        if not pai: return 0

        node = Node(valor)

        pai.filhos.append(node)
        node.pai = pai

    
    def acessar(self, valor):

        return self.acc_rec(valor, self.raiz)

    def acc_rec(self, valor, node):

        if node.valor == valor: return node

        if node.filhos:

            for filho in node.filhos:

                node = self.acc_rec(valor, filho)
                if node: return node
        
        return 0
    
    def varrer(self):

        self.varrec(self.raiz, 0)
    
    def varrec(self, node, indent):

        print("\n|{}Node de valor {}".format("--"*indent, node.valor))

        for i in node.filhos:

            self.varrec(i,indent+1)

a = Arvore()

a.inserir_raiz(20)