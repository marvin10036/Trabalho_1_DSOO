from visao.tela import Tela


class TelaMercado(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome: ")

    def pede_endereco(self):
        return super()._pede_str("Endereco: ")