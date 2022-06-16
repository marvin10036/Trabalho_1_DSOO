from entidade.categoria import Categoria
from visao.tela_categoria import TelaCategoria
from controle.abstract_ctrl import AbstractCtrl
from entidade.usuario import Usuario

class CtrlCategoria(AbstractCtrl):
    def __init__(self):
        self.__tela = TelaCategoria()
        self.__categorias = []
        self.__usuario_logado = None

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def criador(self) -> Categoria:
        self.__tela.imprime_titulo("Nova categoria")
        nome = self.__tela.pede_nome()

        if nome is not None:
            categoria = self.busca(nome)
            if categoria is not None:
                return categoria
            else:
                nova_categoria = Categoria(nome, self.__usuario_logado)
                self.incluir(nova_categoria)
                self.__tela.imprime("[Nova categoria inclusa no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return nova_categoria
        else:
            return None

    def selecionar_categoria(self) -> Categoria:
        self.__tela.imprime("\nSelecione uma categoria.")
        while True:
            opcao = self.__tela.seleciona_categoria(self.listar("CRIAR NOVA CATEGORIA"))
            if opcao == 0:
                return None
            elif opcao == 1:
                self.criador()
            else:
                return self.__categorias[opcao - 2]

    def novo(self, nome: str) -> Categoria:
        try:
            if isinstance(nome, str):
                return Categoria(nome, self.__usuario_logado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("! Falha ao criar categoria: variavel de entrada em formato invalido !")

    def busca(self, nome: str) -> Categoria:
        for categoria in self.__categorias:
            if categoria.nome == nome:
                return categoria
        else:
            return None

    def incluir(self, categoria: Categoria):
        try:
            if isinstance(categoria, Categoria):
                self.__categorias.append(categoria)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("! Falha ao incluir categoria: variavel de entrada em formato invalido !")

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
        return count - 1

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.__tela.seleciona_categoria(self.listar())
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                confirmar = self.__tela.pede_confirmacao(opcao)
                if confirmar:
                    del(self.__categorias[opcao - 1])
                    break

    def alterar(self):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.__tela.seleciona_categoria(self.listar())
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
                        categoria_selecionada.cadastrador = self.__usuario_logado
                        self.__tela.imprime("[Dados alterados com sucesso]")
                        sucesso = True
                        break
            if sucesso:
                break


if __name__ == "__main__":
    ctrl = CtrlCategoria()
    ctrl.selecionar_categoria()