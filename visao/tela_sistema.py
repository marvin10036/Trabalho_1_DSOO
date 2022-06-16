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

    def opcoes_editar_dados(self):
        super().imprime_titulo("Menu principal")
        print("1 - Categorias")
        print("2 - Mercados")
        print("3 - Produtos")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(3)

    def opcoes_menu_categoria(self):
        super().imprime_titulo("Menu Categoria")
        print("1 - Listar categorias")
        print("2 - Nova categoria")
        print("3 - Editar categoria")
        print("4 - Excluir categoria")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(4)

    def opcoes_menu_mercado(self):
        super().imprime_titulo("Menu Mercado")
        print("1 - Listar mercados")
        print("2 - Novo mercado")
        print("3 - Editar mercado")
        print("4 - Excluir mercado")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(4)

    def opcoes_menu_produto(self):
        super().imprime_titulo("Menu Produto")
        print("1 - Listar produtos")
        print("2 - Novo produto")
        print("3 - Editar produto")
        print("4 - Excluir produto")
        print("5 - Detalhes produto")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(5)