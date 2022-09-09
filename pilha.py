class Pilha:
    def __init__(self) -> None:
        self.itens = []

    def empilha(self, elemento):
        self.itens.append(elemento)

    def desempilha(self):
        self.itens.pop()

    def topo(self):
        return self.itens[len(self.itens)-1]

    def __str__(self) -> str:
        s = ''
        for it in reversed(self.itens):
            s += it+'\n'
        return s


    

    