from entidade.preco import Preco
from visao.tela_preco import TelaPreco


class CtrlPreco():
    def __init__(self, usuario_logado):
        self.__tela = TelaPreco()
        self.__usuario_logado = usuario_logado

    def novo(self) -> Preco: #TODO falta especificar tipo cadastrador
        self.__tela.imprime_titulo("Novo preco")
        valor = self.__tela.pede_valor()
        self.__tela.imprime_linha_de_fechamento()

        if valor is not None:
            novo_preco = Preco(valor, cadastrador)
            return novo_preco
        else:
            return None


if __name__ == "__main__":
    CtrlPreco().novo()