from entidade.categoria import Categoria
from visao.tela_categoria import TelaCategoria


class CtrlCategoria():
    def __init__(self):
        self.__tela = TelaCategoria()
        self.__categorias = []

    def novo(self):
        self.__tela.imprime_titulo("Nova categoria")
        nome = self.__tela.pede_nome()

        if nome is not None:
            categoria = self.busca(nome)
            if categoria is not None:
                return categoria
            else:
                nova_categoria = Categoria(nome, "cadastrador") #TODO falta cadastrador
                self.__categorias.append(nova_categoria)
                self.__tela.imprime("[Nova categoria inserida no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return nova_categoria
        else:
            return None

    def busca(self, nome: str):
        for categoria in self.__categorias:
            if categoria.nome == nome:
                return categoria
        else:
            return None



if __name__ == "__main__":
    CtrlCategoria().novo()