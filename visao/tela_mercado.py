from visao.tela import Tela


class TelaMercado(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome: ").capitalize()

    def pede_endereco(self):
        return super()._pede_str("Endereco: ").capitalize()

    def seleciona_mercado(self, n_de_mercados):
        return super()._seleciona_opcao_int(n_de_mercados)