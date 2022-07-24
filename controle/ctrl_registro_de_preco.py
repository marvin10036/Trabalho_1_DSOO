from visao.tela_registro_de_preco import TelaRegistroDePreco
from entidade.registro_de_preco import RegistroDePreco

from entidade.usuario import Usuario
from entidade.mercado import Mercado
from entidade.qualificador import Qualificador
from entidade.preco import Preco
from entidade.produto import Produto

class CtrlRegistroDePreco():
    def __init__(self):
        self.__registros = []
        self.__usuario_logado = None
        self.__tela = TelaRegistroDePreco()

    def set_usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario

    def get_registros(self):
        return self.__registros

    # def excluir_registro(self, registro: RegistroDePreco):
    #     if isinstance(registro, RegistroDePreco):
    #         del(self.__registros[])

    def opcoes_iniciais(self):
        texto = self.__tela.opcoes_iniciais_open()
        self.__tela.tela_close()

        if texto == None:
            return None

        busca = self.pesquisar_produto(texto)
        if busca == None:
            self.__tela.pop_up("Falha", "Produto nao encontrado")
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

    def novo(self, produto: Produto, qualificadores_preenchidos: list, preco: Preco, mercado: Mercado):
        if isinstance(produto, Produto) and \
                isinstance(preco, Preco) and \
                isinstance(mercado, Mercado) and \
                self.__valida_formato_qualificadores(qualificadores_preenchidos):
            return RegistroDePreco(produto, qualificadores_preenchidos, preco, mercado,
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
            if registro.produto.nome == registro_a_comparar.produto.nome and \
                    registro.mercado == registro_a_comparar.mercado and \
                    self.__valida_igualdade_qualificadores(registro, registro_a_comparar):
                return registro
        else:
            return None

    def mostrar_lista_completa(self):
        if len(self.__registros) == 0:
            self.__tela.imprime("Nenhum registro foi realizado ainda")
        else:
            self.printar_lista(self.__registros)

    def pesquisar_produto(self, texto: str):
        registros_produto = []
        produto = texto.split(" ", 1)[:-1]
        try:
            produto = produto[0]
        except:
            produto = texto
        qualificadores = texto.split(" ", 1)[1:]

        for registro in self.__registros:
            if registro.produto.nome.upper() == produto.upper():
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
        opcao = self.__tela.opcao_ordenacao_open()
        self.__tela.tela_close()

        if opcao == 1:
            self.printar_lista(lista)
        elif opcao == 2:
            lista_ordenada = self.ordenar_por_preco(lista)
            self.printar_lista(lista_ordenada)
        elif opcao == 3:
            lista_ordenada = self.ordenar_por_confirmacoes(lista)
            self.printar_lista(lista_ordenada)
        elif opcao == 4:
            lista_ordenada = self.ordernar_por_data(lista)
            self.printar_lista(lista_ordenada)
        else:
            return None

    def ordenar_por_preco(self, lista): #A ideia e que retorne em uma
        for registro in lista:          #com apenas os qualificadores
            for i in range(0, len(registro.precos)-1):
                for j in range(len(registro.precos)-1):
                    if registro.precos[i].valor > registro.precos[i+1].valor:
                        variavel_auxiliar = registro.precos[i]
                        registro.precos[i] = registro.precos[i+1]
                        registro.precos[i+1] = variavel_auxiliar
        return lista

    def ordenar_por_confirmacoes(self,lista):
        for registro in lista:                        #mesma logica de ordencao do anterior
            for i in range(0, len(registro.precos)-1):
                for j in range(len(registro.precos)-1):
                    if registro.precos[i].confirmacoes > registro.precos[i+1].confirmacoes:
                        variavel_auxiliar = registro.precos[i]
                        registro.precos[i] = registro.precos[i+1]
                        registro.precos[i+1] = variavel_auxiliar
        return lista[::-1]

    def ordernar_por_data(self,lista):
        for registro in lista:                        #mesma logica de ordencao dos anteriores
            for i in range(0, len(registro.precos)-1):
                for j in range(len(registro.precos)-1):
                    if registro.precos[i].data > registro.precos[i+1].data:
                        variavel_auxiliar = registro.precos[i]
                        registro.precos[i] = registro.precos[i+1]
                        registro.precos[i+1] = variavel_auxiliar
        return lista

    def listar(self, texto_opcao_especial=''):
        self.__tela.imprime_titulo("Lista de registros")
        count = 1

        self.__tela.imprime("0 - Voltar")

        if texto_opcao_especial != '':
            self.__tela.imprime("1 - {}".format(texto_opcao_especial))
            count += 1

        for registro in self.__registros:
            self.__tela.imprime("{}:".format(count))  #dados do objeto
            self.__tela.imprime("- Produto: {}".format(registro.produto.nome))
            for qualificador in registro.qualificadores:
                self.__tela.imprime("- {}: {}".format(qualificador.titulo, qualificador.descricao))
            self.__tela.imprime("- Mercado: {} | End: {}".format(registro.mercado.nome, registro.mercado.endereco))
            for preco in registro.precos:
                self.__tela.imprime("- Preco: R${} | Confirmacoes: {} | Cadastrador: {}".format(preco.valor,
                                                                                                preco.confirmacoes,
                                                                                                preco.cadastrador.nome))
            count += 1

        self.__tela.imprime_linha_de_fechamento()
        return count - 1    #retorna numero de opcoes (sem contar o zero)

    def excluir(self):
        self.__tela.imprime("\nEscolha uma opcao para ser excluida.")
        while True:
            opcao = self.__tela.seleciona_opcao_lista(self.listar())
            if opcao == 0: #voltar
                break
            else:
                confirmar = self.__tela.pede_confirmacao()
                if confirmar:
                    del (self.__registros[opcao - 1])
                    self.__tela.imprime("[item removido da lista de registros]")
                    break

    def printar_lista(self, lista):
        matriz = []
        for registro in lista:
            for preco in registro.precos:
                item = []
                item.append(f"{registro.produto.nome}")
                item.append(f"{self.qualificadores_str(registro.qualificadores)}")
                item.append(f"Mercado: {registro.mercado.nome}")
                item.append(f"Preco: R$ {preco.valor}")
                matriz.append(item)

        self.__tela.printar_lista_open(matriz)
        self.__tela.tela_close()

    def qualificadores_str(self, lista_qualificadores: list):
        texto = ""
        for qualificador in lista_qualificadores:
            texto += f"{qualificador.titulo}: {qualificador.descricao}, "
        texto = texto[:-2]

        return texto

if __name__ == "__main__":
    ctrl = CtrlRegistroDePreco()
