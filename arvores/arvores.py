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


    def remover(self, valor):

        node = self.acessar(valor)

        if not node: return 0
        
        if node.filhos: return 0

        node.pai.filhos.remove(node)
        node.pai = None

        return node


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

    
    def remover(self, valor):

        node = self.acessar(valor)

        if not node: return 0
        
        if node.fa or node.fb: return 0

        pai = node.pai
        
        if pai.fa == node: pai.fa = None
        if pai.fb == node: pai.fb = None
            
        node.pai = None

        return node

    
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

class ArvoreBusca:

    def __init__(self):

        self.raiz = None
    
    
    def inserir_raiz(self, raiz):

        if not self.raiz: 
            self.raiz = Node(raiz)
            return 1

        return 0

    def inserir(self, valor):

        pai = self.raiz
        node = Node(valor)

        while 1:

            if valor == pai.valor:

                return 0

            elif valor < pai.valor:

                if pai.fa: pai = pai.fa
                else:
                    pai.fa = node
                    node.pai = pai
                    break
            
            else:

                if pai.fb: pai = pai.fb
                else:
                    pai.fb = node
                    node.pai = pai
                    break
        return 1


    def remover(self, valor):

        node = self.acessar(valor)

        if not node: return 0
        
        if node.fa or node.fb: return 0

        pai = node.pai
        
        if pai.fa == node: pai.fa = None
        if pai.fb == node: pai.fb = None
            
        node.pai = None

        return node

    
    def acessar(self, valor, node = 0):

        if not node: node = self.raiz

        if node.valor == valor: return node
        
        res = 0

        if valor < node.valor: res = self.acessar(valor, node.fa)
        else: res = self.acessar(valor, node.fa)            
        
        return res

    
    def varrer(self, node=0, indent=0):

        if not node: node = self.raiz

        print("|{}{}".format("--"*indent, node.valor))

        if node.fa: self.varrer(node.fa,indent+1)
        if node.fb: self.varrer(node.fb,indent+1)


class AVL:

    def __init__(self):

        self.raiz = None
    
    def inserir_raiz(self, raiz):

        if not self.raiz: 
            self.raiz = Node(raiz)
            return 1

        return 0

    def inserir(self, valor):

        pai = self.raiz
        node = Node(valor)

        while 1:

            if valor == pai.valor:

                return 0

            elif valor < pai.valor:

                if pai.fa: pai = pai.fa
                else:
                    pai.fa = node
                    node.pai = pai
                    break
            
            else:

                if pai.fb: pai = pai.fb
                else:
                    pai.fb = node
                    node.pai = pai
                    break
        return 1
    
    def altura(self, node):

        if not node: return 0
        else: return 1 + max(self.altura(node.fa), self.altura(node.fb))
    
    def fator(self, node):

        fe = self.altura(node.fa)
        fd = self.altura(node.fb)

        return -fe+fd

    def acessar(self, valor, node = 0):

        if not node: node = self.raiz

        if node.valor == valor: return node
        
        res = 0

        if valor < node.valor: res = self.acessar(valor, node.fa)
        else: res = self.acessar(valor, node.fa)            
        
        return res

    
    def varrer(self, node=0, indent=0):

        if not node: node = self.raiz

        print("|{}{}".format("--"*indent, node.valor))

        if node.fa: self.varrer(node.fa,indent+1)
        if node.fb: self.varrer(node.fb,indent+1)

    
            

a = AVL()

a.inserir_raiz(21)
