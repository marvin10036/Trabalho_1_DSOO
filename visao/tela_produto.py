from visao.tela import Tela


class TelaProduto(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome: ")

    def pede_descricao(self):
        return super()._pede_str("Descricao: ")