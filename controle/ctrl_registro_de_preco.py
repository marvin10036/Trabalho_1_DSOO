from visao.tela_registro_de_preco import TelaRegistroDePreco
from entidade.registro_de_preco import RegistroDePreco

from entidade.usuario import Usuario
from entidade.mercado import Mercado
from entidade.qualificador import Qualificador
from entidade.preco import Preco


class CtrlRegistroDePreco():
    def __init__(self):
        self.__registros = []
        self.__usuario_logado = None
        self.__tela = TelaRegistroDePreco()

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def get_registros(self):
        return self.__registros

    def opcoes_iniciais(self):
        busca = self.__tela.printar_opcoes_iniciais()
        busca = self.pesquisar_produto(busca)
        if busca == None:
            return None
        elif len(busca[1]) == 0: #se nao tiver qualificadores
            self.menu_ordenacao(busca[0])
        else:
            filtragem_extra = self.produzir_lista_filtrada_produto_qualifica(busca[0], busca[1])
            self.menu_ordenacao(filtragem_extra)

    def __valida_formato_qualificadores(self, qualificadores: list) -> bool:
        for qualificador in qualificadores:
            if not isinstance(qualificador, Qualificador):
                return False
        else:
            return True

    def novo(self, nome_produto: str, qualificadores_preenchidos: list, preco: Preco, mercado: Mercado):
        if isinstance(nome_produto, str) and \
                isinstance(preco, Preco) and \
                isinstance(mercado, Mercado) and \
                self.__valida_formato_qualificadores(qualificadores_preenchidos):
            return RegistroDePreco(nome_produto, qualificadores_preenchidos, preco, mercado,
                                   self.__usuario_logado.nome)
        else:
            return None

    def incluir(self, registro: RegistroDePreco):
        if isinstance(registro, RegistroDePreco):
            self.__registros.append(registro)

    def __valida_igualdade_qualificadores(self, registro: RegistroDePreco, registro_a_comparar: RegistroDePreco):
        for n in range(len(registro.qualificadores)):
            if registro.qualificadores[n].descricao != registro_a_comparar.qualificadores[n].descricao:
                return False
        else:
            return True

    def buscar(self, registro_a_comparar: RegistroDePreco):
        for registro in self.__registros:
            if registro.nome_produto == registro_a_comparar.nome_produto and \
                    registro.mercado == registro_a_comparar.mercado and \
                    self.__valida_igualdade_qualificadores(registro, registro_a_comparar):
                return registro
        else:
            return None

    def mostrar_lista_completa(self):
        if len(self.__registros) == 0:
            self.__tela.imprime("Nenhum registro foi realizado ainda")
        else:
            self.__tela.printar_lista(self.__registros)

    def pesquisar_produto(self, texto: str):
        registros_produto = []
        produto = texto.split(" ", 1)[:-1]
        try:
            produto = produto[0]
        except:
            produto = texto
        qualificadores = texto.split(" ", 1)[1:]
        for registro in self.__registros:
            if registro.nome_produto.upper() == produto.upper():
                registros_produto.append(registro)
        if len(registros_produto) == 0:
            self.__tela.imprime("Produto nao encontrado")
            return None
        else:
            return [registros_produto, qualificadores]

    def produzir_lista_filtrada_produto_qualifica(self, lista_base: list, qualificadores: list):
        lista_retornada = []
        for registro in lista_base:
            for qualificador_presente in registro.qualificadores:
                for i in qualificadores:
                    if i.upper() == qualificador_presente.descricao.upper():
                        lista_retornada.append(registro)

        return(lista_retornada)

    def menu_ordenacao(self, lista):
        opcao = self.__tela.mostrar_opcao_ordenacao()
        if opcao == 1:
            self.__tela.printar_lista(lista)
        elif opcao == 2:
            lista_ordenada = self.ordenar_por_preco(lista)
            self.__tela.printar.lista(lista_ordenada)
        elif opcao == 3:
            lista_ordenada = self.ordenar_por_confirmacoes(lista)
            self.__tela.printar_lista(lista_ordenada)
        else:
            lista_ordenada = self.ordernar_por_data(lista)
            self.__tela.printar_lista(lista_ordenada)

    def ordenar_por_preco(self, lista):
        """
        lista_retornada = []
        contador = 1
        while contador != 0:
            contador = 0
            for registro in lista:
                for i in range(len(registro.precos)):
                    if registro.precos[i].valor < valor_anterior:
                        posicao = lista.index(registro)
                        lista.insert()

                    valor_anterior = registro
        """

    def ordenar_por_confirmacoes(self,lista):
        pass

    def ordernar_por_data(self,lista):
        pass






if __name__ == "__main__":
    ctrl = CtrlRegistroDePreco()
