
class Categoria():
    def __init__(self, nome: str, cadastrador: str):
        self.__nome = nome
        self.__cadastrador = cadastrador

    @property
    def nome(self):
        return self.__nome

    @property
    def cadastrador(self):
        return self.__cadastrador

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cadastrador.setter
    def cadastrador(self, cadastrador):
        self.__cadastrador = cadastrador
