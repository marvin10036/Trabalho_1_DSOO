from entidade.preco import Preco
from visao.tela_preco import TelaPreco


class CtrlPreco():
    def __init__(self):
        self.__tela = TelaPreco()

    def novo(self) -> list:
        valor = self.__tela.pede_dados()
        if valor != None:
            novo_preco = Preco(valor, "cadastrador") #TODO falta cadastrador
            return novo_preco
        else:
            return None


if __name__ == "__main__":
    CtrlPreco().novo()