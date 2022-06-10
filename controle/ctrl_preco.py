from entidade.preco import Preco
from visao.tela_preco import TelaPreco


class CtrlPreco():
    def __init__(self):
        self.__tela = TelaPreco()

    def novo(self) -> Preco:
        print("entrou em novo")
        valor = self.__tela.pedeDados()
        novoPreco = Preco(valor, "cadastrador") #TODO falta cadastrador
        return novoPreco


if __name__ == "__main__":
    CtrlPreco().novo()