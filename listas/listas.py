from node import Node

class LS:

    def __init__(self):

        self.lista = [None]
        self.tamanho = 0

    def inserir(self, node, *args):

        pos = self.tamanho

        if args: pos = args[0]

        if pos > self.tamanho: return False

        for i in range(pos, self.tamanho): self.lista[i+1] = self.lista[i]

        self.lista[pos] = node
        self.tamanho += 1
        self.lista.append(None)

        return True


    def remover(self, pos):

        if self.tamanho < pos: return 0

        node = self.lista[pos]

        for i in range(pos, self.tamanho): self.lista[i] = self.lista[i+1]

        del self.lista[self.tamanho]

        self.tamanho -= 1

        return node



    def varrer(self):

        for i in range(self.tamanho): print(self.lista[i])


class LE:

    def __init__(self):

        self.raiz = None


    def shift(self, node):

        node.prox = self.raiz
        self.raiz = node


    def push(self, node):

        if not self.raiz: return self.shift(node)

        n = self.raiz

        while n.prox: n = n.prox


        n.prox = node

    def varrer(self):

        node = self.raiz

        while node: print(node); node = node.prox


    def kill(self, valor):

        node = self.raiz

        if node.valor == valor:

            self.raiz = node.prox
            del node
            return


        while node.prox:

            if node.prox.valor == valor:

                target = node.prox
                node.prox = target.prox

                del target
                return

            node = node.prox


    def count_it(self):

        node = self.raiz

        r = 0

        while node: 
            
            r+=1
            node = node.prox

        return r


    def count_rec(self):
        
        return self.cr(self.raiz)


    def cr(self, node):

        if not node: return 0
        return 1 + self.cr(node.prox)

    def ord(self):

        o = 1

        node = self.raiz

        while node and node.prox:

            if node > node.prox: o = 1; break
            node = node.prox

        return bool(o)

    
    def min_rec(self):

        return self.mr(self.raiz, self.raiz).valor

    def mr(self, node, m):

        if not node: return m
        
        if node.valor < m.valor: m = node
        return self.mr(node.prox, m)


    def min_it(self):

        m = self.raiz

        while node:

            if node.valor < m.valor: m = node
            node = node.prox
        
        return node



lista = LE()

lista.push(Node(3))
lista.push(Node(5))
lista.shift(Node(7))
print('hi')




