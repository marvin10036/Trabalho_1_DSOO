from controle.ctrl_registro_de_preco import CtrlRegistroDePreco
from visao.tela_sistema import TelaSistema

from controle.ctrl_categoria import CtrlCategoria
from controle.ctrl_mercado import CtrlMercado
from controle.ctrl_qualificador import CtrlQualificador
from controle.ctrl_preco import CtrlPreco
from controle.ctrl_produto import CtrlProduto

from entidade.usuario import Usuario
from entidade.produto import Produto
from entidade.registro_de_preco import RegistroDePreco

class CtrlSistema():
    def __init__(self):
        self.__tela = TelaSistema()
        self.__usuario_logado = None

        self.__ctrl_registro = CtrlRegistroDePreco()
        self.__ctrl_categoria = CtrlCategoria()
        self.__ctrl_mercado = CtrlMercado()
        self.__ctrl_preco = CtrlPreco()
        self.__ctrl_qualificador = CtrlQualificador()
        self.__ctrl_produto = CtrlProduto()

    def __setar_usuario_logado(self, usuario_logado: Usuario):
        self.__ctrl_registro.set_usuario_logado(usuario_logado)
        self.__ctrl_produto.set_usuario_logado(usuario_logado)
        self.__ctrl_mercado.set_usuario_logado(usuario_logado)
        self.__ctrl_categoria.set_usuario_logado(usuario_logado)


    def __login(self):
        while True:
            usuario = "joao"
            if usuario != None: #TODO usuario retornado com sucesso
                self.__setar_usuario_logado(usuario)
                return True
            else:
                self.__tela.imprime("Usuario nao encontrado. Tente novamente.")

    def programa_principal(self):
        if self.__login():
            while True:
                opcao = self.__tela.opcoes_menu_principal()
                self.__tela.imprime_linha_de_fechamento()

                if opcao == 0:
                    break
                elif opcao == 1:
                    self.novo_registro()
                elif opcao == 2:
                    self.buscar_registro()
                elif opcao == 3:
                    self.editar_dados()

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    #utilizar esse metodo para criar produto, ja que essa classe possui as entidades necessarias para criacao
    def criar_novo_produto(self, nome_produto=''):

        if nome_produto == '':
            nome_produto = self.__tela.pede_nome_produto()

        self.__tela.imprime("Escolha uma categoria para o produto.")
        categoria = self.__ctrl_categoria.selecionar_categoria()

        self.__tela.imprime("Crie um conjunto de qualificadores para o produto. Exemplo: 'Marca' e 'Peso'")
        novos_qualificadores = self.__ctrl_qualificador.criador(com_descricao=False)

        produto = self.__ctrl_produto.criador(novos_qualificadores,
                                           categoria,
                                           nome_produto)
        return produto

    def __preencher_qualificadores(self, produto: Produto):
        qualificadores_preenchidos = []

        for qualificador in produto.qualificadores:
            descricao = self.__tela.pede_descricao_qualificador("{}: ".format(qualificador.titulo))
            qualificador_preenchido = self.__ctrl_qualificador.novo(qualificador.titulo, descricao)
            qualificadores_preenchidos.append(qualificador_preenchido)

        return qualificadores_preenchidos

    def novo_registro(self):
        try:
            self.__tela.imprime_titulo("Novo registro de preco.")

            self.__tela.imprime("Primeiramente, insira o nome do produto: ")
            nome_produto = self.__tela.pede_nome_produto()
            produto = self.__ctrl_produto.busca(nome_produto)

            #se nao encontrar um produto na lista de produtos com o mesmo nome
            if produto is None:
                quer_criar_produto = self.__tela.pede_confirmacao("Produto nao encontrado. Deseja criar um novo?")

                if quer_criar_produto is False:
                    return
                else:
                    produto = self.criar_novo_produto(nome_produto)
                    if produto is None:
                        raise Exception

            self.__tela.imprime("Preencha os qualificadores do produto visto.")
            qualificadores_preenchidos = self.__preencher_qualificadores(produto)

            self.__tela.imprime("Forneca o valor do preco visto.")
            preco = self.__ctrl_preco.criador()
            if preco is None:
                raise Exception

            self.__tela.imprime("Selecione o mercado onde o preco foi visto.")
            mercado = self.__ctrl_mercado.selecionar_mercado()
            if mercado is None:
                raise Exception

            self.__tela.imprime("\nFALTA CRIAR REGISTRO E ETC\n")

            #TODO implementar logica para criacao de registro
            #TODO verificar se ja existe um registro igual ou criar um novo
            #TODO verificar caso exista um registro igual se há um preco igual e somar no contador dele

            # novo_registro = self.__ctrl_registro.novo(nome_produto,
            #                                           qualificadores_preenchidos,
            #                                           preco,
            #                                           mercado)
            #
            # registro_existente = self.__ctrl_registro.buscar(novo_registro)

        except Exception:
            self.__tela.imprime("Falha na criacao do registro - alguma variavel nao foi preenchida.")

        self.__tela.imprime("Criacao de registro de preco finalizada.")
        self.__tela.imprime_linha_de_fechamento()

    def buscar_registro(self):
        pass

    def editar_dados(self):
        pass

if __name__ == "__main__":
    CtrlSistema().programa_principal()