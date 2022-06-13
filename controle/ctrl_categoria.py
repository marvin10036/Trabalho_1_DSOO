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

    def listar(self, texto_opcao_especial=''):
        self.__tela.imprime_titulo("Lista de categorias")
        count = 1

        self.__tela.imprime("0 - Voltar")

        if texto_opcao_especial != '':
            self.__tela.imprime("1 - {}".format(texto_opcao_especial))
            count += 1

        for categoria in self.__categorias:
            self.__tela.imprime("{} - Categoria: {}.".format(count, categoria.nome))
            count += 1

        self.__tela.imprime_linha_de_fechamento()
        return self.__tela.seleciona_categoria(count - 1)

    def selecionar_categoria(self, usuario_logado):
        self.__tela.imprime("\nSelecione uma categoria.")
        while True:
            opcao = self.listar("CRIAR NOVA CATEGORIA")
            if opcao is None:
                return None
            elif opcao == 0:
                self.novo(usuario_logado)
            else:
                return self.__categorias[opcao - 1]

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                confirmar = self.__tela.pede_confirmacao(opcao)
                if confirmar:
                    del(self.__categorias[opcao - 1])
                    break

    def alterar(self, cadastrador: str):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                categoria_selecionada = self.__categorias[opcao - 1]
                while True:
                    nome = self.__tela.pede_nome()
                    for categoria in self.__categorias:
                        if categoria.nome == nome:
                            self.__tela.imprime("Ja existe categoria com esse nome.")
                            break
                    else:
                        categoria_selecionada.nome = nome
                        sucesso = True
                        break
            if sucesso:
                break


if __name__ == "__main__":
    ctrl = CtrlCategoria()
    ctrl.novo("joao")
    ctrl.alterar("joao")