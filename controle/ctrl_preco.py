from entidade.preco import Preco
from visao.tela_preco import TelaPreco


class CtrlPreco():
    def __init__(self):
        self.__tela = TelaPreco()

    def novo(self) -> list:
        valor = self.__tela.pedeDados()
        if valor != None:
            novoPreco = Preco(valor, "cadastrador") #TODO falta cadastrador
            return novoPreco
        else:
            return None


if __name__ == "__main__":
    CtrlPreco().novo()