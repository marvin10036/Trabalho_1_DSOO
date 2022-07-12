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

    #cria objeto caso nao exista um igual na lista de objetos, insere na lista e retorna o objeto
    def criador(self) -> Mercado:
        self.__tela.imprime_titulo("Novo mercado")
        nome = self.__tela.pede_nome()
        endereco = self.__tela.pede_endereco()

        if nome is not None and endereco is not None:
            mercado = self.busca(nome, endereco)
            if mercado is not None:
                self.__tela.imprime("Ja existe um mercado com esses dados.")
                self.__tela.imprime("[Mercado selecionado]")
                self.__tela.imprime_linha_de_fechamento()
                return mercado
            else:
                novo_mercado = Mercado(nome, endereco, self.__usuario_logado)
                self.incluir(novo_mercado)
                self.__tela.imprime("[Novo mercado inserido no sistema]")
                self.__tela.imprime_linha_de_fechamento()
                return novo_mercado
        else:
            return None

    def menu_mercado(self):
        self.selecionar_mercado()

    def selecionar_mercado(self) -> Mercado:
        while True:
            opcoes = []
            count = 0
            for mercado in self.__mercados:
                count += 1
                opcoes.append("{} - Nome: {}. End: {}.".format(count, mercado.nome, mercado.endereco))

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
                    return self.__mercados[opcao_selecionada]

            elif botao == 'NOVO':
                dados = self.__tela.menu_criacao('Registre o mercado')
                if dados is None:
                    return None
                else:
                    novo = self.novo(dados[0], dados[1])
                    self.incluir(novo)

            elif botao == 'EXCLUIR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao excluir:', 'Favor selecionar uma opcao para excluir.')
                else:
                    del(self.__mercados[opcao_selecionada])

            elif botao == 'EDITAR':
                if opcao_selecionada is None:
                    self.__tela.pop_up('Erro ao editar:', 'Favor selecionar uma opcao para editar.')
                else:
                    dados = self.__tela.menu_criacao('Insira as novas informacoes')
                    if dados is None:
                        return None
                    else:
                        self.__mercados[opcao_selecionada].nome = dados[0]
                        self.__mercados[opcao_selecionada].endereco = dados[1]
                        self.__mercados[opcao_selecionada].cadastrador = self.__usuario_logado
            else:
                return None

    def novo(self, nome: str, endereco: str) -> Mercado:
        try:
            if isinstance(nome, str) and isinstance(endereco, str):
                return Mercado(nome, endereco, self.__usuario_logado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("! Falha ao criar objeto: variavel de entrada em formato invalido !")

    def busca(self, nome: str, endereco: str):
        for mercado in self.__mercados:
            if mercado.nome == nome and mercado.endereco == endereco:
                return mercado
        else:
            return None

    def incluir(self, mercado: Mercado):
        try:
            if isinstance(mercado, Mercado):
                self.__mercados.append(mercado)
            else:
                raise TypeError
        except TypeError:
            self.__tela.imprime("! Falha ao incluir mercado: variavel de entrada em formato invalido !")

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
        return count - 1

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.__tela.seleciona_mercado(self.listar())
            if opcao == 0:
                break
            else:
                confirmar = self.__tela.pede_confirmacao()
                if confirmar:
                    del(self.__mercados[opcao - 1])
                    break

    def alterar(self):
        self.__tela.imprime("\nEscolha uma opcao para ser alterada.")
        while True:
            opcao = self.__tela.seleciona_mercado(self.listar())
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
                        self.__tela.imprime("[Dados alterados com sucesso]")
                        sucesso = True
                        break
            if sucesso:
                break

if __name__ == "__main__":
    mercado = CtrlMercado().selecionar_mercado()