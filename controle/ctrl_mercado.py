from entidade.mercado import Mercado
from visao.tela_mercado import TelaMercado


class CtrlMercado():
    def __init__(self):
        self.__mercados = []
        self.__tela = TelaMercado()
