from controle.ctrl_categoria import CtrlCategoria
from controle.ctrl_mercado import CtrlMercado
from controle.ctrl_qualificador import CtrlQualificador
from controle.ctrl_preco import CtrlPreco
from controle.ctrl_produto import CtrlProduto

from visao.tela_registro_de_preco import TelaRegistroDePreco

from entidade.registro_de_preco import RegistroDePreco


class CtrlRegistroDePreco():
    def __init__(self):
        self.__registros = []
        self.__tela = TelaRegistroDePreco()
        self.__ctrl_categoria = CtrlCategoria()
        self.__ctrl_mercado = CtrlMercado()
        self.__ctrl_qualificador = CtrlQualificador()
        self.__ctrl_preco = CtrlPreco()
        self.__ctrl_produto = CtrlProduto()
        self.__usuario_logado = "usuario"

    def novo_registro(self): #todo revisar tudo
        while True:
            self.__tela.imprime_titulo("Novo registro de preco.")

            self.__tela.imprime("Primeiramente, insira o nome do produto: ")
            nome_produto = self.__tela.pede_nome_produto()
            produto = self.__ctrl_produto.busca(nome_produto)

            if produto is None:
                self.__tela.imprime("Produto nao encontrado: sera criado um novo com o nome inserido.")

                self.__tela.imprime("Escolha uma categoria para o produto.")
                categoria = self.__ctrl_categoria.listar(self.__usuario_logado)

                self.__tela.imprime("Crie um conjunto de qualificadores para o produto. Exemplo: 'Marca' e 'Peso'")
                novos_qualificadores = self.__ctrl_qualificador.novo(com_descricao=False)

                produto = self.__ctrl_produto.novo(novos_qualificadores,
                                                   categoria,
                                                   self.__usuario_logado,
                                                   nome_produto)

            self.__tela.imprime("Preencha os qualificadores do produto visto.")
            qualificadores_preenchidos = []
            for qualificador in produto.qualificadores:
                descricao = self.__tela.pede_descricao_qualificador("{}: ".format(qualificador.titulo))
                qualificador_preenchido = self.__ctrl_qualificador.novo_objeto_qualificador(qualificador.titulo,
                                                                                            descricao)
                qualificadores_preenchidos.append(qualificador_preenchido)

            self.__tela.imprime("Forneca o valor do preco visto.")
            preco = self.__ctrl_preco.novo(self.__usuario_logado)

            self.__tela.imprime("Selecione o mercado onde o preco foi visto.")
            mercado = self.__ctrl_mercado.listar(self.__usuario_logado)

            for registro in self.__registros: #todo arrumar checagem
                if registro.nome_produto == nome_produto:
                    print("ja existe")
            else:
                novo_registro = RegistroDePreco(nome_produto,
                                                qualificadores_preenchidos,
                                                preco,
                                                mercado,
                                                self.__usuario_logado)
                self.__registros.append(novo_registro)



if __name__ == "__main__":
    ctrl = CtrlRegistroDePreco()
    ctrl.novo_registro()