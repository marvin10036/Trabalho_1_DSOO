from entidade.categoria import Categoria
from visao.tela_categoria import TelaCategoria


class CtrlCategoria():
    def __init__(self):
        self.__tela = TelaCategoria()

if __name__ == "__main__":
    CtrlCategoria().novo()