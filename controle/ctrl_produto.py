from entidade.produto import Produto
from visao.tela_produto import TelaProduto

class CtrlProduto():
    def __init__(self):
        self.__produtos = []
        self.__tela = TelaProduto()