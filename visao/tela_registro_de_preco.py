from visao.tela import Tela


class TelaRegistroDePreco(Tela):
    def teste(self):
        pass

    def printar_opcoes_iniciais(self):
        self.imprime_linha_de_fechamento()
        self.imprime_titulo("Menu de busca")
        self.imprime_linha_de_fechamento()
        pesquisar = input("Escreva o produto que quer buscar. Eh pertido a insercao de apenas um qualificador"
                          " por vez separado por espaco: ")

        return pesquisar

    def printar_lista(self, lista):
        self.imprime_linha_de_fechamento()
        self.imprime_titulo("Lista")
        self.imprime_linha_de_fechamento()
        for registro in lista:
            for preco in registro.precos:
                print (f"{registro.nome_produto}, "
                       f"{self.qualificadores_str(registro.qualificadores)}",
                       f"|Mercado: {registro.mercado.nome}",
                       f"|Preco: R$ {preco.valor}")


    def mostrar_opcao_ordenacao(self):
        self.imprime_linha_de_fechamento()
        self.imprime_titulo("Opcoes de ordenacao")
        self.imprime_linha_de_fechamento()
        self.imprime("Escolha por qual meio gostaria de ordenar: \n1 - Nenhum \n2 - Preco"
                     " \n3 - Numero de confirmacoes \n4 -Data de postagem")

        return self._seleciona_opcao_int_restrito(4)


    def qualificadores_str(self, lista_qualificadores: list):
        texto = ""
        for qualificador in lista_qualificadores:
            texto += f"{qualificador.titulo}: {qualificador.descricao}, "
        texto = texto[:-2]

        return texto
