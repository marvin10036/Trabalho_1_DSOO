from controle.ctrl_registro_de_preco import CtrlRegistroDePreco
from visao.tela_sistema import TelaSistema

from controle.ctrl_categoria import CtrlCategoria
from controle.ctrl_mercado import CtrlMercado
from controle.ctrl_qualificador import CtrlQualificador
from controle.ctrl_preco import CtrlPreco
from controle.ctrl_produto import CtrlProduto
from controle.ctrl_usuario import CtrlUsuario

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
        self.__ctrl_usuario = CtrlUsuario()

    def setar_usuario_geral(self, usuario_logado: Usuario):
        self.__usuario_logado = usuario_logado
        self.__ctrl_registro.set_usuario_logado(usuario_logado)
        self.__ctrl_produto.set_usuario_logado(usuario_logado)
        self.__ctrl_mercado.set_usuario_logado(usuario_logado)
        self.__ctrl_categoria.set_usuario_logado(usuario_logado)
        self.__ctrl_preco.set_usuario_logado(usuario_logado)

    def login(self):
        usuario = self.__ctrl_usuario.login()
        if usuario != None:
            self.setar_usuario_geral(usuario)
            return True

    def signup(self):
        usuario = self.__ctrl_usuario.signup()
        if usuario != None:
            while True:
                self.__tela.imprime_linha_de_fechamento()
                self.__tela.imprime_titulo("PESSOA JURIDICA DEVE SER VINCULADA A UM MERCADO")
                estabelecimento = self.__ctrl_mercado.selecionar_mercado()
                if estabelecimento != None:
                    usuario.estabelecimento = estabelecimento
                    break

    def programa_principal(self):
        while True:
            nao_fechar = self.__menu_usuario()
            if not (nao_fechar):
                break
            self.menu_principal()

    def menu_principal(self):
        while True:
            opcao = self.__tela.opcoes_menu_principal()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.criar_novo_registro()
            elif opcao == 2:
                self.buscar_registro()
            elif opcao == 3:
                self.editar_dados()

    # utilizar esse metodo para criar produto,
    # ja que esta classe (CtrlSistema) possui as entidades necessarias para criacao
    def criar_novo_produto(self, nome_produto='') -> Produto:

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

    def criar_novo_registro(self):
        if self.__usuario_logado.cadastrouHoje:
            self.__tela.imprime("Voce ja realizou um cadastro hoje, espere ate amanha")
            return

        try:
            self.__tela.imprime_titulo("Novo registro de preco.")

            self.__tela.imprime("Primeiramente, insira o nome do produto: ")
            nome_produto = self.__tela.pede_nome_produto()
            produto = self.__ctrl_produto.busca(nome_produto)

            # se nao encontrar um produto na lista de produtos com o mesmo nome
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

            if self.__ctrl_usuario.retorna_tipo(self.__usuario_logado) == "PessoaJuridica":
                self.__tela.imprime_titulo("Usuario pessoa juridica detectado, foi selecionado o mercado vinculado")
                mercado = self.__usuario_logado.estabelecimento
            else:
                self.__tela.imprime("Selecione o mercado onde o preco foi visto.")
                mercado = self.__ctrl_mercado.selecionar_mercado()
                if mercado is None:
                    raise Exception

            novo_registro = self.__ctrl_registro.novo(nome_produto,
                                                      qualificadores_preenchidos,
                                                      preco,
                                                      mercado)

            registro_existente = self.__ctrl_registro.buscar(novo_registro)
            if registro_existente != None:
                registro_existente.incluir_preco(novo_registro.precos[0])
                self.__tela.imprime_linha_de_fechamento()
                self.__tela.imprime_titulo("Registro de produto ja existente. Adicionando preco.")
                self.__tela.imprime_linha_de_fechamento()
            else:
                self.__ctrl_registro.incluir(novo_registro)
                self.__tela.imprime_linha_de_fechamento()
                self.__tela.imprime_titulo("Registro realizado com sucesso")
                self.__tela.imprime_linha_de_fechamento()

            self.__usuario_logado.cadastrouHoje = True
        except Exception:
            self.__tela.imprime("Falha na criacao do registro - alguma variavel nao foi preenchida.")
            self.__usuario_logado.cadastrouHoje = False

        self.__tela.imprime("Criacao de registro de preco finalizada.")
        self.__tela.imprime_linha_de_fechamento()


    def __preencher_qualificadores(self, produto: Produto):
        qualificadores_preenchidos = []

        for qualificador in produto.qualificadores:
            descricao = self.__tela.pede_descricao_qualificador("{}: ".format(qualificador.titulo))
            qualificador_preenchido = self.__ctrl_qualificador.novo(qualificador.titulo, descricao)
            qualificadores_preenchidos.append(qualificador_preenchido)

        return qualificadores_preenchidos

    def buscar_registro(self):
        self.__ctrl_registro.opcoes_iniciais()

    def editar_dados(self):
        while True:
            opcao = self.__tela.opcoes_editar_dados()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.__menu_categoria()
            elif opcao == 2:
                self.__menu_mercado()
            elif opcao == 3:
                self.__menu_produto()
            elif opcao == 4:
                self.__menu_registros()

    def __menu_registros(self):
        while True:
            opcao = self.__tela.opcoes_menu_registro()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.__ctrl_registro.listar()
            elif opcao == 2:
                self.criar_novo_registro()
            elif opcao == 3:
                self.__ctrl_registro.excluir()

    def __menu_categoria(self):
        while True:
            opcao = self.__tela.opcoes_menu_categoria()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.__ctrl_categoria.listar()
            elif opcao == 2:
                self.__ctrl_categoria.criador()
            elif opcao == 3:
                self.__ctrl_categoria.alterar()
            elif opcao == 4:
                self.__ctrl_categoria.excluir()

    def __menu_mercado(self):
        while True:
            opcao = self.__tela.opcoes_menu_mercado()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.__ctrl_mercado.listar()
            elif opcao == 2:
                self.__ctrl_mercado.criador()
            elif opcao == 3:
                self.__ctrl_mercado.alterar()
            elif opcao == 4:
                self.__ctrl_mercado.excluir()

    def __menu_produto(self):
        while True:
            opcao = self.__tela.opcoes_menu_produto()
            self.__tela.imprime_linha_de_fechamento()

            if opcao == 0:
                break
            elif opcao == 1:
                self.__ctrl_produto.listar()
            elif opcao == 2:
                self.criar_novo_produto()
            elif opcao == 3:
                self.__ctrl_produto.alterar()
            elif opcao == 4:
                self.__ctrl_produto.excluir()
            elif opcao == 5:
                produto_selecionado = self.__ctrl_produto.selecionar_produto()
                if produto_selecionado != None:
                    self.__detalhes_produto(produto_selecionado)

    def __detalhes_produto(self, produto: Produto):
        self.__tela.imprime_titulo("Detalhes produto")
        self.__tela.imprime("Nome: {}".format(produto.nome))
        self.__tela.imprime("Descricao: {}".format(produto.descricao))
        self.__tela.imprime("Categoria: {}".format(produto.categoria.nome))
        self.__tela.imprime("Qualificadores:")
        for qualificador in produto.qualificadores:
            self.__tela.imprime("- {}".format(qualificador.titulo))
        self.__tela.imprime("Cadastrador: {}".format(produto.cadastrador.nome))
        self.__tela.imprime_linha_de_fechamento()

    def __menu_usuario(self):
        while True:
            condicao = False
            opcao = self.__tela.opcoes_menu_usuario()
            self.__tela.imprime_linha_de_fechamento()
            if opcao == 0:
                return False
            elif opcao == 1:
                self.signup()
            elif opcao == 3:
                self.passa_um_dia()
            else:
                condicao = self.login()
                if condicao:
                    return True

    def passa_um_dia(self):
        self.__ctrl_usuario.setta_cadastrou_usuarios()
        self.__tela.imprime("Sistema movido um dia a frente")

if __name__ == "__main__":
    CtrlSistema().programa_principal()
