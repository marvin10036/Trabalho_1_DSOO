from visao.tela import Tela


class TelaCategoria(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome da categoria: ")

    def seleciona_categoria(self, quantidade: int):
        return super()._seleciona_opcao_int(quantidade)

    def pede_confirmacao(self, opcao):
        return super()._pergunta_sim_ou_nao("Tem certeza que deseja excluir a opcao {}?".format(opcao))