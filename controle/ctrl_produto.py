from entidade.produto import Produto
from visao.tela_produto import TelaProduto

from entidade.usuario import Usuario
from entidade.qualificador import Qualificador
from entidade.categoria import Categoria

class CtrlProduto:
    def __init__(self):
        self.__produtos = []
        self.__tela = TelaProduto()
        self.__usuario_logado = None

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def criador(self, qualificadores, categoria, nome = ''):
        self.__tela.imprime_titulo("Novo produto")
        if nome == '':
            nome = self.__tela.pede_nome()
        else:
            self.__tela.imprime("Nome: {}".format(nome))
        descricao = self.__tela.pede_descricao()

        if nome is not None and descricao is not None:
            produto = self.busca(nome)
            if produto is not None:
                return produto
            else:
                novo_produto = Produto(categoria, nome, descricao, qualificadores, self.__usuario_logado)
                self.__produtos.append(novo_produto)
                self.__tela.imprime("[Novo produto inserido no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return novo_produto
        else:
            self.__tela.imprime("[Falha na criacao do produto]")
            self.__tela.imprime_linha_de_fechamento()
            return None

    def novo(self, categoria: Categoria, nome: str, descricao: str, qualificadores: list):
        try:
            if isinstance(categoria, Categoria) and \
                    isinstance(nome, str) and \
                    isinstance(descricao, str) and \
                    self.__valida_formato_qualificadores(qualificadores):
                return Produto(categoria, nome, descricao, qualificadores, self.__usuario_logado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("! Falha ao criar objeto: variavel de entrada em formato invalido !")

    def busca(self, nome: str):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        else:
            return None

    def incluir(self, produto: Produto):
        try:
            if isinstance(produto, Produto):
                self.__produtos.append(produto)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("Falha ao incluir produto: variavel de entrada em formato invalido")

    def listar(self, texto_opcao_especial=''):
        self.__tela.imprime_titulo("Lista de produtos")
        count = 1

        self.__tela.imprime("0 - Voltar")

        if texto_opcao_especial != '':
            self.__tela.imprime("1 - {}".format(texto_opcao_especial))
            count += 1

        for produto in self.__produtos:
            self.__tela.imprime("{} - {} - Descricao: {}.".format(count, produto.nome, produto.descricao))
            count += 1

        self.__tela.imprime_linha_de_fechamento()
        return count - 1

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.__tela.seleciona_opcao(self.listar())
            if opcao == 0: #voltar
                break
            else:
                confirmar = self.__tela.pede_confirmacao()
                if confirmar:
                    del (self.__produtos[opcao - 1])
                    self.__tela.imprime("[Produto excluido com sucesso]")
                    break

    def alterar(self):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.__tela.seleciona_opcao(self.listar())
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                produto_selecionado = self.__produtos[opcao - 1]
                while True:

                    nome = self.__tela.pede_nome()
                    descricao = self.__tela.pede_descricao()

                    for produto in self.__produtos:
                        if produto.nome == nome and produto.descricao == descricao:
                            self.__tela.imprime("Ja existe um produto com esses dados.")
                            break
                    else:
                        produto_selecionado.nome = nome
                        produto_selecionado.descricao = descricao
                        produto_selecionado.cadastrador = self.__usuario_logado
                        self.__tela.imprime("[Dados alterados com sucesso]")
                        sucesso = True
                        break
            if sucesso:
                break

    def selecionar_produto(self):
        self.__tela.imprime("\nSelecione um produto.")
        while True:
            opcao = self.__tela.seleciona_opcao(self.listar())
            if opcao == 0:
                return None
            else:
                return self.__produtos[opcao - 2]



    def __valida_formato_qualificadores(self, qualificadores: list) -> bool:
        for qualificador in qualificadores:
            if not isinstance(qualificador, Qualificador):
                return False
        else:
            return True


if __name__ == "__main__":
    ctrl = CtrlProduto()
