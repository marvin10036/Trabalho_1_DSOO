from entidade.preco import Preco
from visao.tela_preco import TelaPreco

from entidade.usuario import Usuario

class CtrlPreco():
    def __init__(self):
        self.__tela = TelaPreco()
        self.__usuario_logado = None

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def criador(self) -> Preco: #TODO falta especificar tipo cadastrador
        self.__tela.imprime_titulo("Novo preco")
        valor = self.__tela.pede_valor()
        self.__tela.imprime_linha_de_fechamento()

        if valor is not None:
            novo_preco = Preco(valor, self.__usuario_logado)
            return novo_preco
        else:
            return None

    def novo(self, valor: float):
        if isinstance(valor, float):
            return Preco(valor, self.__usuario_logado)


if __name__ == "__main__":
    CtrlPreco().criador()