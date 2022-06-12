from visao.tela import Tela


class TelaCategoria(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome da categoria: ")

    def seleciona_categoria(self, n_de_categorias):
        return super()._seleciona_opcao_int(n_de_categorias)
