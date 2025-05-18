class VariavelLimitada:
    def __init__(self, maximo):
        self.maximo = maximo
        self.minimo = 0  # mínimo fixo inicial
        self._valor = maximo  # começa cheio

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = max(self.minimo, min(self.maximo, novo_valor))

    def definir_minimo(self, novo_minimo):
        self.minimo = novo_minimo
        if self._valor < self.minimo:
            self._valor = self.minimo

    def __str__(self):
        return f"{self.valor}/{self.maximo} (mín: {self.minimo})"