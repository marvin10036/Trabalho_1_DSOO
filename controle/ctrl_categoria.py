from entidade.categoria import Categoria
from visao.tela_categoria import TelaCategoria
from controle.abstract_ctrl import AbstractCtrl
from entidade.usuario import Usuario
from persistencia.DAO_categoria import DAOCategoria

class CtrlCategoria(AbstractCtrl):
    def __init__(self):
        self.__mercados = []
        self.__DAO_proprio = DAOCategoria()
        self.__tela = TelaCategoria()
        self.__usuario_logado = None

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def __lista_de_objetos(self):
        #return self.__mercados
        return list(self.__DAO_proprio.get_all())

    def menu(self):
        while True:
            opcoes = []
            count = 0
            for objeto in self.__lista_de_objetos():
                count += 1
                opcoes.append("{} - Nome: {}.".format(count, objeto.nome)) #TODO revisar

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
                dados = self.__tela.menu_criacao('Registre a categoria.') #TODO revisar
                if dados is None:
                    return None
                else:
                    novo = self.novo(dados[0]) #TODO revisar
                    if novo is not None:
                        self.incluir(novo)

            elif botao == 'EXCLUIR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao excluir:', 'Favor selecionar uma opcao para excluir.')
                else:
                    objeto = self.__lista_de_objetos()[opcao_selecionada]
                    self.excluir(objeto)

            elif botao == 'EDITAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao editar:', 'Favor selecionar uma opcao para editar.')
                else:
                    self.alterar(opcao_selecionada)
            else:
                return None

    def novo(self, nome: str):
        try:
            if isinstance(nome, str): #TODO revisar
                return Categoria(nome, self.__usuario_logado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao criar objeto:", "Variavel de entrada em formato invalido.")
            return None

    def busca(self, nome: str):
        for objeto in self.__lista_de_objetos():
            if objeto.nome == nome: #TODO revisar
                return objeto
        else:
            return None

    def incluir(self, objeto_novo):
        try:
            if isinstance(objeto_novo, Categoria): #TODO revisar
                for objeto in self.__lista_de_objetos():
                    if objeto.nome == objeto_novo.nome: #TODO revisar
                        raise TypeError
                else:
                    #self.__lista_de_objetos().append(objeto_novo)
                    self.__DAO_proprio.add(objeto_novo)
                    self.__tela.pop_up("Sucesso.", "Objeto incluido no sistema.")
            else:
                raise TypeError
        except TypeError:
            self.__tela.pop_up("Falha ao incluir objeto:", "Variavel de entrada em formato invalido.")
        except Exception:
            self.__tela.pop_up("Falha ao incluir objeto:", "Ja incluido no sistema.")

    def excluir(self, objeto):
        self.__DAO_proprio.remove(objeto.nome)

    def alterar(self, index_opcao):
        objeto_selecionado = self.__lista_de_objetos()[index_opcao]
        while True:
            dados = self.__tela.menu_criacao('Insira as novas informacoes.')
            if dados is None:
                return None
            else:
                nome = dados[0] #TODO revisar

                for objeto in self.__lista_de_objetos():
                    if objeto.nome == nome: #TODO revisar
                        self.__tela.pop_up("Problema:", "Ja existe uma categoria com esses dados.") #TODO revisar
                        break
                else: #TODO revisar
                    self.excluir(objeto_selecionado)
                    self.incluir(self.novo(nome))
                    return True


if __name__ == "__main__":
    objeto = CtrlCategoria().menu()