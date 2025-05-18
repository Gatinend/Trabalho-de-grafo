
from extras import VariavelLimitada
from no import Agua, Arvore, Brigadista


class Caminhao:

    def __init__ (self,nome,posicao,capacidade):
        self.nome = nome
        self.posicao = posicao
        self.carga = VariavelLimitada(capacidade)
        self.em_transito = False
        self.trajeto = []

    def apagar_fogo(self, queimando, apagados):
        # Verifica se o nó atual (posição do caminhão) é uma árvore
        if isinstance(self.posicao, Arvore):

            # Verifica se essa árvore está pegando fogo
            if self.posicao.queimando:
                
                # Calcula quanto ainda falta apagar (quanto está queimando)
                esta_queimando = self.posicao.potencia_queima.maximo - self.posicao.potencia_queima.valor

                # Caso a carga do caminhão seja suficiente para apagar tudo:
                if self.carga.valor >= esta_queimando:
                    self.posicao.queimando = False               # Fogo completamente apagado
                    apagados.append(self.posicao)                # Marca como apagado
                    queimando.remove(self.posicao)               # Remove da lista de nós queimando
                    print(f" {self.posicao.nome}: fogo completamente apagado.")
                    self.posicao.set_estado_final("apagado")
                # Caso só dê pra apagar parcialmente:
                elif self.carga.valor < esta_queimando:
                    # Apaga o máximo possível com a carga atual
                    # E atualiza o valor mínimo para refletir que aquela parte já foi queimada
                    # (Ou seja, o que já foi apagado não poderá voltar a queimar)
                    self.posicao.potencia_queima.valordefinir_minimo(self.carga.valor)

                    # Reduz a carga do caminhão com base no quanto foi apagado
                    self.carga.valor -= esta_queimando

                    # Exibe a energia de fogo restante após a tentativa de apagar
                    print(f"{self.posicao.nome} é uma árvore com {self.posicao.potencia_queima.valor} de energia restante.")
    
    
    def coletar_agua(self):
        # Verifica se a posição atual é um ponto de reabastecimento de água
        # Neste caso, um nó do tipo 'Brigadista' (talvez seja um posto ou base de abastecimento)
        if isinstance(self.posicao, Brigadista):
            self.carga = self.carga.maximo  # Recarrega totalmente a carga de água

        # Verifica se a posição atual é um nó com água disponível (ex: lago, rio, etc.)
        elif isinstance(self.posicao, Agua):
            self.carga = self.carga.maximo  # Também recarrega totalmente a carga de água
    
    def montar_trageto(self):

        
