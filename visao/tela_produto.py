from visao.tela import Tela


class TelaProduto(Tela):
    def pede_nome(self):
        return super()._pede_str("Nome: ")

    def pede_descricao(self):
        return super()._pede_str("Descricao: ")

    def seleciona_opcao(self, n_de_opcoes):
        return super()._seleciona_opcao_int(n_de_opcoes)

    def pede_confirmacao(self):
        return super()._pergunta_sim_ou_nao("Tem certeza que deseja excluir o produto selecionado?")