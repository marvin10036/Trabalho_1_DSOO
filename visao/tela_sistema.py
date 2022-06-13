from visao.tela import Tela


class TelaSistema(Tela):
    def teste(self):
        pass

    def opcoes_menu_principal(self) -> int:
        super().imprime_titulo("Menu principal")
        print("1 - Novo registro de preco")
        print("2 - Buscar registro de preco")
        print("3 - Editar dados do sistema")
        print("0 - Finalizar programa")
        return super()._seleciona_opcao_int(3)

    def pede_nome_produto(self):
        return super()._pede_str("Nome do produto: ")

    def pede_descricao_qualificador(self, titulo: str):
        return input(titulo)

    def pede_confirmacao(self, texto: str):
        return super()._pergunta_sim_ou_nao(texto)