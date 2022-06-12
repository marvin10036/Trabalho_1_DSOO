from entidade.qualificador import Qualificador
from entidade.preco import Preco
from entidade.mercado import Mercado

#TODO falta cadastrador aqui
class RegistroDePreco():
    def __init__(self, nome_produto, qualificadores: list, preco: Preco, mercado: Mercado, cadastrador: str):
        self.__nome_produto = nome_produto
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
    def nome_produto(self):
        return self.__nome_produto

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
