from entidade.mercado import Mercado
from visao.tela_mercado import TelaMercado


class CtrlMercado():
    def __init__(self):
        self.__mercados = []
        self.__tela = TelaMercado()

    def novo(self, cadastrador) -> Mercado: #TODO falta especificar tipo do cadastrador
        self.__tela.imprime_titulo("Novo mercado")
        nome = self.__tela.pede_nome()
        endereco = self.__tela.pede_endereco()

        if nome is not None and endereco is not None:
            mercado = self.busca(nome, endereco)
            if mercado is not None:
                return mercado
            else:
                novo_mercado = Mercado(nome, endereco, cadastrador)
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

    def listar(self, usuario_logado):
        self.__tela.imprime_titulo("Lista de mercados")
        count = 1
        for mercado in self.__mercados:
            self.__tela.imprime("{} - {} - Endereco: {}.".format(count, mercado.nome, mercado.endereco))
            count += 1
        self.__tela.imprime("0 - CRIAR NOVO MERCADO")
        self.__tela.imprime_linha_de_fechamento()

        return self.__tela.seleciona_mercado(len(self.__mercados))


    def selecionar_mercado(self, usuario_logado):
        while True:
            opcao = self.listar("CRIAR NOVO MERCADO")
            if opcao is None:
                return None
            elif opcao == 0:
                self.novo(usuario_logado)
            else:
                return self.__mercados[opcao - 1]



if __name__ == "__main__":
    ctrl = CtrlMercado()
    ctrl.selecionar_mercado()