from visao.tela import Tela


class TelaCategoria(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome da categoria: ")

    def seleciona_categoria(self, quantidade: int):
        return super()._seleciona_opcao_int(quantidade)
