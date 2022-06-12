from entidade.produto import Produto
from visao.tela_produto import TelaProduto
from controle.ctrl_qualificador import CtrlQualificador

class CtrlProduto:
    def __init__(self):
        self.__produtos = []
        self.__tela = TelaProduto()

    def novo(self):
        self.__tela.imprime_titulo("Novo produto")
        nome = self.__tela.pede_nome()
        descricao = self.__tela.pede_descricao()

        if nome is not None and descricao is not None:
            produto = self.busca(nome)
            if produto is not None:
                return produto
            else:
                novo_produto = Produto(nome, descricao, "cadastrador")  # TODO falta cadastrador
                self.__produtos.append(novo_produto)
                self.__tela.imprime("[Novo produto inserido no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return novo_produto
        else:
            self.__tela.imprime("[Falha na criacao do produto]")
            self.__tela.imprime_linha_de_fechamento()
            return None

    def busca(self, nome: str):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        else:
            return None

if __name__ == "__main__":
    ctrl = CtrlProduto()
    ctrl.novo()
