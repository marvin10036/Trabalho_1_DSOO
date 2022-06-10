from datetime import date


class Preco():
    def __init__(self, valor: float, cadastrador: str):
        self.__data = date.today().strftime("%d/%m/%Y")
        self.__valor = valor
        self.__confirmacoes = 1
        self.__cadastrador = cadastrador #TODO falta classe usuario

    @property
    def data(self):
        return self.__data

    @property
    def valor(self):
        return self.__valor

    @property
    def confirmacoes(self):
        return self.__confirmacoes

    @property
    def cadastrador(self):
        return self.__cadastrador
