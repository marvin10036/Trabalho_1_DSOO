


class Produto():
    def __init__(self, nome: str, descricao: str, cadastrador: str):
        self.__categoria = None
        self.__nome = nome
        self.__descricao = descricao
        self.__qualificadores = None
        self.__cadastrador = cadastrador

    @property
    def categoria(self):
        return self.__categoria

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def cadastrador(self):
        return self.__cadastrador

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @qualificadores.setter
    def qualificadores(self, qualificadores):
        self.__qualificadores = qualificadores

    @cadastrador.setter
    def cadastrador(self, cadastrador):
        self.__cadastrador = cadastrador