from entidade.produto import Produto
from visao.tela_produto import TelaProduto

from entidade.usuario import Usuario
from controle.ctrl_qualificador import CtrlQualificador
from controle.ctrl_categoria import CtrlCategoria
from entidade.qualificador import Qualificador
from entidade.categoria import Categoria

class CtrlProduto:
    def __init__(self):
        self.__produtos = []
        self.__tela = TelaProduto()
        self.__usuario_logado = None
        self.ctrl_categoria = CtrlCategoria()

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def preencher_qualificadores(self, produto: Produto):
        nome_qualificadores = []
        for qualificador in produto.qualificadores:
            nome_qualificadores.append(qualificador.titulo)

        valores_preenchidos = self.__tela.preencher_qualificadores(nome_qualificadores)
        if valores_preenchidos is None:
            return None
        else:
            qualificadores_preenchidos = []

            x = 0
            for qualificador in produto.qualificadores:
                qualificador_preenchido = CtrlQualificador().novo(qualificador.titulo, valores_preenchidos[x])
                qualificadores_preenchidos.append(qualificador_preenchido)
                x += 1
            return qualificadores_preenchidos

    def __valida_formato_qualificadores(self, qualificadores: list) -> bool:
        for qualificador in qualificadores:
            if not isinstance(qualificador, Qualificador):
                return False
        else:
            return True

    def __lista_de_objetos(self):
        return self.__produtos

    def menu(self):
        while True:
            opcoes = []
            count = 0
            for objeto in self.__lista_de_objetos():
                count += 1
                opcoes.append("{} - Nome: {}. Desc: {}.".format(count, objeto.nome, objeto.descricao)) #TODO revisar

            botao, opcao_selecionada = self.__tela.menu_opcoes(opcoes)

            print(botao)
            print(opcao_selecionada)

            # processa os botoes/valores lidos
            if botao is None:
                return None

            elif botao == 'SELECIONAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao selecionar:', 'Favor selecionar uma opcao.')
                else:
                    return self.__lista_de_objetos()[opcao_selecionada]

            elif botao == 'NOVO':
                dados = self.__tela.menu_criacao('Registre o produto.') #TODO revisar
                if dados is None:
                    return None
                else:
                    self.__tela.pop_up("Proximo passo:", "Selecione uma categoria para o produto.")
                    categoria = self.ctrl_categoria.menu()
                    if categoria is None:
                        return None
                    else:
                        self.__tela.pop_up("Proximo passo:", "Crie qualificadores para o produto.")
                        qualificadores = CtrlQualificador().criador(com_descricao=False)
                        if qualificadores is None:
                            return None
                        else:
                            novo = self.novo(categoria, dados[0], dados[1], qualificadores)
                            if novo is not None:
                                self.incluir(novo)

            elif botao == 'EXCLUIR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao excluir:', 'Favor selecionar uma opcao para excluir.')
                else:
                    self.excluir(opcao_selecionada)

            elif botao == 'EDITAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao editar:', 'Favor selecionar uma opcao para editar.')
                else:
                    self.alterar(opcao_selecionada)
            else:
                return None

    def novo(self, categoria: Categoria, nome: str, descricao: str, qualificadores):
        try:
            if isinstance(nome, str) and isinstance(descricao, str) \
                    and isinstance(categoria, Categoria) and self.__valida_formato_qualificadores(qualificadores):
                return Produto(categoria, nome, descricao, qualificadores, self.__usuario_logado) #todo falta tratar duplicado
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao criar objeto:", "Variavel de entrada em formato invalido.")
            return None

    def busca(self, nome: str):
        for objeto in self.__lista_de_objetos():
            if objeto.nome == nome:
                return objeto
        else:
            return None

    def incluir(self, objeto_novo):
        try:
            if isinstance(objeto_novo, Produto):
                for objeto in self.__lista_de_objetos():
                    if objeto.nome == objeto_novo.nome and objeto.descricao == objeto_novo.descricao:
                        raise TypeError
                else:
                    self.__lista_de_objetos().append(objeto_novo)
                    self.__tela.pop_up("Sucesso.", "Objeto incluido no sistema.")
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao incluir objeto:", "Variavel de entrada em formato invalido.")
        except Exception:
            self.__tela.pop_up("Falha ao incluir objeto:", "Ja incluido no sistema.")

    def excluir(self, index_opcao):
        del self.__lista_de_objetos()[index_opcao]

    def alterar(self, index_opcao):
        objeto_selecionado = self.__lista_de_objetos()[index_opcao]
        while True:
            dados = self.__tela.menu_criacao('Insira as novas informacoes.')
            if dados is None:
                return None
            else:
                nome = dados[0]
                descricao = dados[1]

                for objeto in self.__lista_de_objetos():
                    if objeto.nome == nome and objeto.descricao == descricao: #TODO revisar
                        self.__tela.pop_up("Problema:", "Ja existe um mercado com esses dados.") #TODO revisar
                        break
                else:
                    objeto_selecionado.nome = nome
                    objeto_selecionado.descricao = descricao
                    objeto_selecionado.cadastrador = self.__usuario_logado
                    return True



if __name__ == "__main__":
    ctrl = CtrlProduto()
    ctrl.selecionar_produto()
