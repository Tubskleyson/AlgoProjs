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


    def acessar(self, valor, node = 0):

        if not node: node = self.raiz

        if node.valor == valor: return node

        if node.filhos:

            for filho in node.filhos:

                node = self.acessar(valor, filho)
                if node: return node
        
        return 0

    
    def varrer(self, node=0, indent=0):

        if not node: node = self.raiz

        print("|{}{}".format("--"*indent, node.valor))

        for i in node.filhos:

            self.varrer(i,indent+1)

class ArvoreBin:

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

        if not pai.fa: pai.fa = node
        elif not pai.fb: pai.fb = node
        else: return 0
        
        node.pai = pai

    
    def acessar(self, valor, node = 0):

        if not node: node = self.raiz

        if node.valor == valor: return node
        
        res = 0

        if node.fa: res = self.acessar(valor, node.fa)
        
        if not res and node.fb: res = self.acessar(valor, node.fb)

        if res: return res                
        
        return 0

    
    def varrer(self, node=0, indent=0):

        if not node: node = self.raiz

        print("|{}{}".format("--"*indent, node.valor))

        if node.fa: self.varrer(node.fa,indent+1)
        if node.fb: self.varrer(node.fb,indent+1)

            

a = ArvoreBin()

a.inserir_raiz(20)
