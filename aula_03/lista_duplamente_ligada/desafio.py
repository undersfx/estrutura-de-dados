class ListaVaziaErro(Exception):
    pass


class Noh():
    def __init__(self, valor, esquerdo=None, direito=None) -> None:
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito


class ListaDuplamenteLigada():
    def __init__(self) -> None:
        self.tam = 0
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, valor):
        self.tam += 1
        noh = Noh(valor)
        if self.primeiro is None:
            self.primeiro = noh
            self.ultimo = noh
        else:
            noh.esquerdo = self.ultimo
            self.ultimo.direito = noh
            self.ultimo = noh

    def adicionar_a_esquerda(self, valor):
        self.tam += 1
        noh = Noh(valor)
        if self.primeiro is None:
            self.primeiro = noh
            self.ultimo = noh
        else:
            noh.direito = self.primeiro
            self.primeiro.esquerdo = noh
            self.primeiro = noh

    def remover(self):
        if self.primeiro is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.ultimo is self.primeiro:
            noh = self.primeiro
            self.primeiro = None
            self.ultimo = None
        else:
            noh = self.ultimo
            self.ultimo = noh.esquerdo
            self.ultimo.direito = None
        self.tam -= 1
        return noh.valor

    def remover_a_esquerda(self):
        if self.primeiro is None:
            raise ListaVaziaErro('Não existem elementos na lista')
        elif self.ultimo is self.primeiro:
            noh = self.primeiro
            self.primeiro = None
            self.ultimo = None
        else:
            noh = self.primeiro
            self.primeiro = noh.direito
            self.primeiro.esquerdo = None
        self.tam -= 1
        return noh.valor

    def __iter__(self):
        noh = self.primeiro
        while noh is not None:
            yield noh.valor
            noh = noh.direito