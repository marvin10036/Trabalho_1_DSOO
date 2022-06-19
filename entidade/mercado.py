


class Mercado():
    def __init__(self, nome: str, endereco: str, cadastrador):
        self.__nome = nome
        self.__endereco = endereco
        self.__cadastrador = cadastrador

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cadastrador(self):
        return self.__cadastrador

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @cadastrador.setter
    def cadastrador(self, cadastrador):
           self.__cadastrador = cadastrador
