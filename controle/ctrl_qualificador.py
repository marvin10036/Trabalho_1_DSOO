from entidade.qualificador import Qualificador
from visao.tela_qualificador import TelaQualificador


class CtrlQualificador():
    def __init__(self):
        self.__tela = TelaQualificador()

    def __imprime_qualificadores(self, qualificadores: list):
        self.__tela.imprime_titulo("Qualificadores")

        for qualificador in qualificadores:
            titulo = qualificador.titulo
            descricao = qualificador.descricao
            self.__tela.imprime_qualificador(titulo, descricao)

        self.__tela.imprime_linha_de_fechamento()

    def criador(self, com_descricao = True):
        inserindo = True
        lista_qualificadores = []

        self.__tela.imprime_titulo("Novo conjunto de qualificadores")
        while inserindo is True:
            titulo = self.__tela.pede_titulo(lista_qualificadores)

            if com_descricao:
                descricao = self.__tela.pede_descricao()
            else:
                descricao = ''

            #and (descricao is not None)
            if (titulo is not None):
                lista_qualificadores.append(Qualificador(titulo, descricao))
                self.__imprime_qualificadores(lista_qualificadores)
                inserindo = self.__tela.continuar("[Qualificador criado com sucesso]")
            else:
                self.__imprime_qualificadores(lista_qualificadores)
                inserindo = self.__tela.continuar("[Qualificador nao foi criado: "
                                                  "valor inválido inserido em um dos campos]")

        if len(lista_qualificadores) != 0:
            self.__tela.imprime_linha_de_fechamento()
            return lista_qualificadores
        else:
            self.__tela.imprime("[Qualificadores nao foram criados]")
            self.__tela.imprime_linha_de_fechamento()
            return None

    def novo(self, titulo: str, descricao: str):
        if isinstance(titulo, str) and isinstance(descricao, str):
            return Qualificador(titulo, descricao)
        else:
            return None




# teste da classe controle
if __name__ == "__main__":
    ctrl = CtrlQualificador()
    ctrl.criador()
