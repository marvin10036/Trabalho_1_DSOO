from datetime import date
#TODO falta classe usuario

class Preco():
    def __init__(self, valor: float, cadastrador: str):
        self.__data = date.today().strftime("%d/%m/%Y")
        self.__valor = valor
        self.__cadastrador = cadastrador  # TODO falta classe usuario
        self.__confirmacoes = 1

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

    @data.setter
    def data(self, data):
        self.__data = data

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @confirmacoes.setter
    def confirmacoes(self, confirmacoes):
        self.__confirmacoes = confirmacoes

    @cadastrador.setter
    def cadastrador(self, cadastrador):
        self.__cadastrador = cadastrador

    def somaConfirmacao(self, confirmacao: int):
        self.__confirmacoes += confirmacao
