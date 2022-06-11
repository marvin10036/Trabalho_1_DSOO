from visao.tela import Tela


class TelaCategoria(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome da categoria: ")
