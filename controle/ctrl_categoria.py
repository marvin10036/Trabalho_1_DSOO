from entidade.categoria import Categoria
from visao.tela_categoria import TelaCategoria


class CtrlCategoria():
    def __init__(self):
        self.__tela = TelaCategoria()
        self.__categorias = []

    def novo(self, cadastrador): #TODO falta especificar tipo
        self.__tela.imprime_titulo("Nova categoria")
        nome = self.__tela.pede_nome()

        if nome is not None:
            categoria = self.busca(nome)
            if categoria is not None:
                return categoria
            else:
                nova_categoria = Categoria(nome, cadastrador)
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

    def listar(self, usuario_logado):
        while True:
            self.__tela.imprime_titulo("Lista de categorias")
            count = 1
            for categoria in self.__categorias:
                self.__tela.imprime("{} - Categoria: {}.".format(count, categoria.nome))
                count += 1
            self.__tela.imprime("0 - CRIAR NOVA CATEGORIA")
            opcao = self.__tela.seleciona_categoria(len(self.__categorias))

            self.__tela.imprime_linha_de_fechamento()

            if opcao is None:
                return None
            elif opcao == 0:
                self.novo(usuario_logado)
            else:
                return self.__categorias[opcao - 1]


if __name__ == "__main__":
    CtrlCategoria().listar()