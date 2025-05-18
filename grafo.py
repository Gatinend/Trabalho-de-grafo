
from no import Brigadista,Agua,Arvore


class Grafo:
    def __init__(self):
        self.nos = {}  # nome -> No

    def adicionar_no(self, nome, tipo, potencia):
        if nome not in self.nos:
            if tipo == 0:
                self.nos[nome] = Brigadista(nome)

            elif tipo == 1:
                self.nos[nome] = Agua(nome)
                
            elif tipo == 2:
                self.nos[nome] = Arvore(nome, potencia)
                

    def adicionar_aresta(self, origem, destino, peso):
        if origem in self.nos and destino in self.nos:
            self.nos[origem].adicionar_vizinho(destino, peso)
            self.nos[destino].adicionar_vizinho(origem, peso)  

    