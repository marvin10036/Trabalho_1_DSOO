from entidade.mercado import Mercado
from visao.tela_mercado import TelaMercado
from entidade.usuario import Usuario
from persistencia.DAO_mercado import DAOMercado

class CtrlMercado():
    def __init__(self):
        self.__mercados = []
        self.__DAO_proprio = DAOMercado()
        self.__tela = TelaMercado()
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
                opcoes.append("{} - Nome: {}. End: {}.".format(count, objeto.nome, objeto.endereco)) #TODO revisar

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
                dados = self.__tela.menu_criacao('Registre o mercado.') #TODO revisar
                if dados is None:
                    return None
                else:
                    novo = self.novo(dados[0], dados[1]) #TODO revisar
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

    def novo(self, nome: str, endereco: str):
        try:
            if isinstance(nome, str) and isinstance(endereco, str): #TODO revisar
                return Mercado(nome, endereco, self.__usuario_logado)
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
            if isinstance(objeto_novo, Mercado): #TODO revisar
                for objeto in self.__lista_de_objetos():
                    if objeto.nome == objeto_novo.nome and objeto.endereco == objeto_novo.endereco: #TODO revisar
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
                endereco = dados[1]

                for objeto in self.__lista_de_objetos():
                    if objeto.nome == nome and objeto.endereco == endereco: #TODO revisar
                        self.__tela.pop_up("Problema:", "Ja existe um mercado com esses dados.") #TODO revisar
                        break
                else: #TODO revisar
                    self.excluir(objeto_selecionado)
                    self.incluir(self.novo(nome, endereco))
                    return True



if __name__ == "__main__":
    mercado = CtrlMercado().menu()