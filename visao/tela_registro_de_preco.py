from visao.tela import Tela


class TelaRegistroDePreco(Tela):
    def teste(self):
        pass

    def printar_lista_completa(self, lista):
        print(85*"-")
        texto = "NOME" + (35 * " ") + "|MERCADO" + (14 * " ") + "|PRECO"
        self.imprime(texto)
        print(85 * "-")
        for registro in lista:
            for preco in registro.precos:
                print (f"{registro.nome_produto}, "
                       f" {self.qualificadores_str(registro.qualificadores)}",
                       f"{registro.mercado.nome}",
                       f"{preco.valor}")

    def printar_lista_filtrada(self, lista):
        pass
    def opcao__filtragem(self):
        pass
    def qualificadores_str(self, lista_qualificadores: list):
        texto = ""
        for qualificador in lista_qualificadores:
            texto += f"{qualificador.titulo}: {qualificador.descricao}, "
        texto = texto[-2]

        return texto

