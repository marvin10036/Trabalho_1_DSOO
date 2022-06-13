from abc import ABC, abstractmethod
from visao.tela import Tela


class AbstractCtrl(ABC):
    @abstractmethod
    def __init__(self):
        self.__tela = Tela()  # TODO tela propria do Ctrl
        self.__lista_de_objetos = []

    @abstractmethod
    def novo(self):
        self.__tela.imprime_titulo("Novo")

        #TODO pede dados do objeto
        dado = "ola"

        if dado is not None:
            objeto = self.busca(dado)
            if objeto is not None:
                return objeto
            else:
                novo_objeto = "Objeto criado" #TODO criar aqui o objeto
                self.__lista_de_objetos.append(novo_objeto)
                self.__tela.imprime("[Novo objeto inserido no sistema]") #TODO adaptar texto
                self.__tela.imprime_linha_de_fechamento()
                return novo_objeto
        else:
            return None

    @abstractmethod
    def busca(self, dado):
        for objeto in self.__lista_de_objetos:
            if dado == dado: #TODO colocar condicao para verificar existencia
                return objeto
        else:
            return None

    @abstractmethod
    def incluir(self):
        pass

    @abstractmethod
    def listar(self, texto_opcao_especial=''):
        self.__tela.imprime_titulo("Lista")
        count = 1

        self.__tela.imprime("0 - Voltar")

        if texto_opcao_especial != '':
            self.__tela.imprime("1 - {}".format(texto_opcao_especial))
            count += 1

        for objeto in self.__lista_de_objetos:
            self.__tela.imprime("{} - {}.".format(count, objeto))  # TODO dados do objeto
            count += 1

        self.__tela.imprime_linha_de_fechamento()
        return self.__tela._seleciona_opcao_int(count - 1)  # TODO chamar funcao propria da tela

    @abstractmethod
    def alterar(self):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                objeto_selecionado = self.__lista_de_objetos[opcao - 1] #TODO utilizar a propria lista
                while True:

                    #TODO [PEDIR DADOS DA TELA AQUI]

                    for objeto in self.__lista_de_objetos:
                        if True: #TODO colocar condicao que checa existencia aqui
                            self.__tela.imprime("Ja existe um objeto com esses dados.")
                            break
                    else:
                        #TODO [ALTERA OS DADOS DO OBJETO AQUI]
                        sucesso = True
                        break
            if sucesso:
                break

    @abstractmethod
    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                confirmar = self.__tela._pergunta_sim_ou_nao("Tem certeza?")  # TODO utilizar metodo proprio da tela
                if confirmar:
                    del (self.__lista_de_objetos[opcao - 1])
                    break
