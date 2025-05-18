
from extras import VariavelLimitada


class No:
    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []  # (vizinho, peso)

    def adicionar_vizinho(self, vizinho, peso):
        self.adjacentes.append((vizinho, peso))


class Agua(No):
    def __init__(self, nome):
        super().__init__(nome)
        self.reabastece = True


class Arvore(No):
    def __init__(self, nome, potencia_queima):
        super().__init__(nome, potencia_queima)
        self.tipo = "arvore"
        self._queimando = True
        self._estado_final = None  # Pode ser "apagado" ou "queimado"

    @property
    def queimando(self):
        return self._queimando

    @queimando.setter
    def queimando(self, valor):
        if self._queimando and valor is False:
            # Mudança de True para False, permite e registra motivo depois
            self._queimando = False
            # O motivo precisa ser informado externamente, vamos deixar None por enquanto
            # Você pode criar outro método para definir o estado final, veja abaixo.
        elif not self._queimando and valor is True:
            # Tentou reacender, checa motivo e printa aviso
            if self._estado_final == "apagado":
                print(f"⚠️ {self.nome} já foi apagado e não pode queimar de novo.")
            elif self._estado_final == "queimado":
                print(f"⚠️ {self.nome} já foi totalmente queimado e não pode queimar de novo.")
            else:
                print(f"⚠️ {self.nome} não pode voltar a queimar.")

    def set_estado_final(self, motivo):
        """Define o motivo final do estado, 'apagado' ou 'queimado'."""
        if motivo in ("apagado", "queimado"):
            self._estado_final = motivo
        else:
            raise ValueError("Motivo deve ser 'apagado' ou 'queimado'")


class Brigadista(No):
    def __init__(self, nome):
        super().__init__(nome)
        self.reabastece = True
        self.caminhao = True