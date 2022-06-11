from entidade.qualificador import Qualificador
from entidade.preco import Preco

#TODO falta mercados e cadastrador aqui
class RegistroDePreco():
    def __init__(self, qualificadores: list, precos: list, mercados: list, cadastrador: str):
        self.__qualificadores = qualificadores
        self.__precos = precos
        self.__mercados = mercados
        self.__cadastrador = cadastrador

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores(self):
        return self.__qualificadores