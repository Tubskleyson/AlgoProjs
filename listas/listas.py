from node import Node


class LS:

    def __init__(self):

        self.lista = [None]
        self.tamanho = 0

    def inserir(self, node, *args):

        pos = self.tamanho

        if args: pos = args[0]

        if pos > self.tamanho: return False

        for i in range(pos, self.tamanho): self.lista[i + 1] = self.lista[i]

        self.lista[pos] = node
        self.tamanho += 1
        self.lista.append(None)

        return True

    def remover(self, pos):

        if self.tamanho < pos: return 0

        node = self.lista[pos]

        for i in range(pos, self.tamanho): self.lista[i] = self.lista[i + 1]

        del self.lista[self.tamanho]

        self.tamanho -= 1

        return node

    def varrer(self):

        for i in range(self.tamanho): print(self.lista[i])

class LCS:

    def __init__(self)


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

    def kill_last(self):

        node = self.raiz

        if not node.prox:
            del self.raiz
            return

        while node.prox.prox: node = node.prox

        last = node.prox
        node.prox = None
        del last
        return

    def count_it(self):

        node = self.raiz

        r = 0

        while node:
            r += 1
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

            if node.valor > node.prox.valor: o = 0; break
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
        node = self.raiz

        while node:

            if node.valor < m.valor: m = node
            node = node.prox

        return m

    def clone_rec(self):

        clone = LE()

        return self.clr(self.raiz, clone)

    def clr(self, node, clone):

        if not node: return clone

        clone_node = Node(node.valor)
        clone.push(clone_node)
        return self.clr(node.prox, clone)

    def clone_it(self):

        clone = LE()
        node = self.raiz

        while node:
            clone_node = Node(node.valor)
            clone.push(clone_node)
            node = node.prox

        return clone

    def mid(self):

        l = self.clone_rec()

        if not l.raiz: return None

        while l.raiz.prox:

            l.kill(l.raiz.valor)
            if l.raiz.prox: l.kill_last()

        mid = l.raiz
        del l
        return mid

    def switch(self, ia, ib):

        if ia > ib: ia, ib = ib, ia

        node = self.raiz
        for i in range(1, ib):
            if i == ia: na = node
            node = node.prox

        if ia:

            na.prox.prox, node.prox.prox = node.prox.prox, na.prox.prox
            na.prox, node.prox = node.prox, na.prox

        else:
            self.raiz.prox, node.prox.prox = node.prox.prox, self.raiz.prox
            node.prox, self.raiz = self.raiz, node.prox

    def parse_it(self, vetor):

        for i in vetor: self.push(Node(i))

    def parse_rec(self, vetor):

        self.prc(vetor, 0)

    def prc(self, vetor, index):

        if index >= len(vetor): return
        self.push(Node(vetor[index]))
        self.prc(vetor, index + 1)
        
class LSC:

  def __init__(self, maximo):
    
    self.lista = [None] 
    self.maximo = maximo
    self.tamanho = 0
    self.ultimo = -1    

  def inserir(self, valor):

    print("\nInserindo item de valor {} ".format(valor))

    if self.tamanho == self.maximo:

      print("\n[ ERRO ] Lista cheia")
      return

    pos = self.acessar(None)
    
    self.lista[pos] = Node(valor)
    self.tamanho += 1
    
    if pos == self.ultimo+1:
      
      self.ultimo = pos
      self.lista.append(None)

  def remover(self, valor):

    print("\nProcurando item de valor {} para remoção".format(valor))

    pos = self.acessar(valor)


    if pos < 0: 

      return
    
    self.lista[pos] = None
    self.tamanho -= 1
    print("Item removido")

  def acessar(self, valor):
  
    pos = self.accrec(valor, 0)

    if valor != None:
      if pos >= 0: print("O item de valor {} está na posição {}".format(valor, pos))
      else: print("O item de valor {} não foi encontrado".format(valor))

    return pos
  
  def accrec(self, valor, i):

    if i > self.tamanho: return -1
    if self.lista[i] == valor: return i 
    if self.lista[i] and self.lista[i].valor == valor: return i
    return self.accrec(valor, i+1)
  
  def varrer(self):

    print('\n',self.lista[:-1],'\n')


class LEC:

    def __init__(self):

        self.raiz = None

    def iniciar(self, node):

        node.prox = node
        self.raiz = node

    def last(self):

        node = self.raiz

        while node.prox != self.raiz: node = node.prox

        return node

    def shift(self, node):

        if not self.raiz: self.iniciar(node)
        else:
            node.prox = self.raiz
            self.last().prox = node
            self.raiz = node

    def push(self, node):

        if not self.raiz: self.iniciar(node)

        else:
            self.last().prox = node
            node.prox = self.raiz

    def varrer(self):

        node = self.raiz
        print(node)

        while node.prox != self.raiz:

            print(node.prox)
            node = node.prox

class LDE:

    def __init__(self):

        self.raiz = None
    
    def shift(self, node):

        if not self.raiz: self.raiz = node

        else:

            node.prox = self.raiz
            self.raiz.ant = node
            self.raiz = node

        return 1
    
    def push(self, node):

        n = self.raiz

        if not n: self.raiz = node

        else:
                
            while n.prox: n = n.prox

            n.prox = node
            node.ant = n

        return 1
    
    def get(self, valor):

        node = self.raiz

        if node.valor == valor: return node

        while node and node.prox:

            if node.valor == valor: return node
            node = node.prox
        
        return 0

    def varrer(self):

        node = self.raiz
        
        while node:

            print(node)
            node = node.prox
        
        return 1

class LCD:

    def __init__(self):

        self.raiz = None

    def iniciar(self, node):

        node.prox = node
        node.ant = node
        self.raiz = node

    def last(self):

        return self.raiz.ant
    
    def shift(self, node):

        if not self.raiz: self.iniciar(node)
        
        else:

            node.prox = self.raiz
            node.ant = self.raiz.ant
            self.raiz.ant.prox = node
            self.raiz.ant = node

            self.raiz = node
        
    def push(self, node):

        if not self.raiz: self.iniciar(node)
        
        else:

            self.last().prox = node
            node.ant = self.last()
            node.prox = self.raiz
            self.raiz.ant = node
    
    
    def varrer(self):

        node = self.raiz
        print(node)

        while node.prox != self.raiz:

            print(node.prox)
            node = node.prox

    def get(self, valor):

        node = self.raiz

        while node:

            if node.valor == valor: return node

            node = node.prox
            
            if node == self.raiz: break

        return 0 
