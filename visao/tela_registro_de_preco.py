from visao.tela import Tela


class TelaRegistroDePreco(Tela):
    def pede_nome_produto(self):
        return super()._pede_str("Nome do produto: ")

    def pede_descricao_qualificador(self, titulo: str):
        return input(titulo)
