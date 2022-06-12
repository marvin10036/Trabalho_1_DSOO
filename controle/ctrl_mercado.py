from entidade.mercado import Mercado
from visao.tela_mercado import TelaMercado


class CtrlMercado():
    def __init__(self):
        self.__mercados = []
        self.__tela = TelaMercado()

    def novo(self) -> Mercado:
        self.__tela.imprime_titulo("Novo mercado")
        nome = self.__tela.pede_nome()
        endereco = self.__tela.pede_endereco()

        if nome is not None and endereco is not None:
            mercado = self.busca(nome, endereco)
            if mercado is not None:
                return mercado
            else:
                novo_mercado = Mercado(nome, endereco,"cadastrador") #TODO falta cadastrador
                self.__mercados.append(novo_mercado)
                self.__tela.imprime("[Novo mercado inserido no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return novo_mercado
        else:
            return None

    def busca(self, nome: str, endereco: str):
        for mercado in self.__mercados:
            if mercado.nome == nome and mercado.endereco == endereco:
                return mercado
        else:
            return None

    def listar(self):
        self.__tela.imprime_titulo("Lista de mercados")
        count = 1

        for mercado in self.__mercados:
            self.__tela.imprime("{} - {} - Endereco: {}.".format(count, mercado.nome, mercado.endereco))
        self.__tela.imprime("0 - CRIAR NOVO MERCADO")

        opcao = self.__tela.seleciona_mercado(len(self.__mercados))
        self.__tela.imprime_linha_de_fechamento()

        if opcao is None:
            return None
        elif opcao == 0:
            self.novo()
        else:
            return self.__mercados[opcao - 1]



if __name__ == "__main__":
    ctrl = CtrlMercado()
#    ctrl.novo()
    ctrl.listar()
    ctrl.listar()