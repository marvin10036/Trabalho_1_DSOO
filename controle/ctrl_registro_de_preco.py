from controle.ctrl_categoria import CtrlCategoria
from controle.ctrl_mercado import CtrlMercado
from controle.ctrl_qualificador import CtrlQualificador
from controle.ctrl_preco import CtrlPreco
from controle.ctrl_produto import CtrlProduto


class CtrlRegistroDePreco():
    def __init__(self):
        self.__registros = []
        self.__ctrl_categoria = CtrlCategoria()
        self.__ctrl_mercado = CtrlMercado()
        self.__ctrl_qualificador = CtrlQualificador()
        self.__ctrl_preco = CtrlPreco()
        self.__ctrl_produto = CtrlProduto()
