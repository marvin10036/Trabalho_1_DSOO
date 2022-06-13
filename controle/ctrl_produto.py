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

    def novo(self, qualificadores, categoria, cadastrador, nome = ''): #TODO falta especificar cadastrador
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
                novo_produto = Produto(categoria, nome, descricao, qualificadores, cadastrador)
                self.__produtos.append(novo_produto)
                self.__tela.imprime("[Novo produto inserido no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return novo_produto
        else:
            self.__tela.imprime("[Falha na criacao do produto]")
            self.__tela.imprime_linha_de_fechamento()
            return None

    def novo_objeto_produto(self, categoria: Categoria, nome: str, descricao: str, qualificadores, cadastrador: str):
        return Produto(categoria, nome, descricao, qualificadores, cadastrador)

    def incluir(self, produto: Produto):
        self.__produtos.append(produto)

    def busca(self, nome: str):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        else:
            return None

if __name__ == "__main__":
    ctrl = CtrlProduto()
    ctrl.novo()
