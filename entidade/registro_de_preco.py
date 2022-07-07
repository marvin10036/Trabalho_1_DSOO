from entidade.qualificador import Qualificador
from entidade.preco import Preco
from entidade.mercado import Mercado
from entidade.produto import Produto

class RegistroDePreco():
    def __init__(self, produto: Produto, qualificadores: list, preco: Preco, mercado: Mercado, cadastrador):
        self.__produto = produto
        self.__qualificadores = qualificadores
        self.__precos = []
        self.__precos.append(preco)
        self.__mercado = mercado
        self.__cadastrador = cadastrador

    def incluir_preco(self, novo_preco: Preco):
        for preco in self.__precos:
            if preco.valor == novo_preco.valor:
                preco.soma_confirmacao(1)
                preco.atualiza_data()
                break
        else:
            self.__precos.append(novo_preco)

    @property
    def produto(self):
        return self.__produto

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def precos(self):
        return self.__precos

    @property
    def mercado(self):
        return self.__mercado

    @property
    def cadastrador(self):
        return self.__cadastrador
