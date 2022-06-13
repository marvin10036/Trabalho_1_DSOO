from entidade.mercado import Mercado
from visao.tela_mercado import TelaMercado

from entidade.usuario import Usuario

class CtrlMercado():
    def __init__(self):
        self.__mercados = []
        self.__tela = TelaMercado()
        self.__usuario_logado = None

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def novo(self) -> Mercado: #TODO falta especificar tipo do cadastrador
        self.__tela.imprime_titulo("Novo mercado")
        nome = self.__tela.pede_nome()
        endereco = self.__tela.pede_endereco()

        if nome is not None and endereco is not None:
            mercado = self.busca(nome, endereco)
            if mercado is not None:
                return mercado
            else:
                novo_mercado = Mercado(nome, endereco, self.__usuario_logado)
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

    def incluir(self, mercado: Mercado):
        self.__mercados.append(mercado)

    def selecionar_mercado(self):
        while True:
            opcao = self.listar("NOVO MERCADO")
            if opcao == 0:
                return None
            elif opcao == 1:
                novo = self.novo()
                self.incluir(novo)
                self.__tela.imprime("[Novo mercado inserido no sistema]")
            else:
                return self.__mercados[opcao - 2]


    def listar(self, texto_opcao_especial=''):
        self.__tela.imprime_titulo("Lista de mercados")
        count = 1

        self.__tela.imprime("0 - Voltar")

        if texto_opcao_especial != '':
            self.__tela.imprime("1 - {}".format(texto_opcao_especial))
            count += 1

        for mercado in self.__mercados:
            self.__tela.imprime("{} - {} - Endereco: {}.".format(count, mercado.nome, mercado.endereco))
            count += 1

        self.__tela.imprime_linha_de_fechamento()
        return self.__tela.seleciona_mercado(count - 1)

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                confirmar = self.__tela.pede_confirmacao()
                if confirmar:
                    del(self.__mercados[opcao - 1])
                    break

    def alterar(self):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.listar()
            if opcao is None:
                break
            elif opcao == 0:
                break
            else:
                objeto_selecionado = self.__mercados[opcao - 1]
                while True:
                    nome = self.__tela.pede_nome()
                    endereco = self.__tela.pede_endereco()

                    for mercado in self.__mercados:
                        if mercado.nome == nome and mercado.endereco == endereco:
                            self.__tela.imprime("Ja existe um mercado com esses dados.")
                            break
                    else:
                        objeto_selecionado.nome = nome
                        objeto_selecionado.endereco = endereco
                        objeto_selecionado.cadastrador = self.__usuario_logado

                        sucesso = True
                        break
            if sucesso:
                break

if __name__ == "__main__":
    mercado = CtrlMercado().selecionar_mercado()
    if mercado == None:
        print("erro")