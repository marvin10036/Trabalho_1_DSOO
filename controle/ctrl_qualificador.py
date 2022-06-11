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
        self.__tela.linha_de_fechamento()

    def novo(self) -> list:
        inserindo = True
        lista_qualificadores = []

        while inserindo is True:
            titulo = self.__tela.pede_titulo()
            descricao = self.__tela.pede_descricao()

            if (titulo is not None) and (descricao is not None):
                lista_qualificadores.append(Qualificador(titulo, descricao))
                self.__imprime_qualificadores(lista_qualificadores)
                inserindo = self.__tela.continuar("Qualificador criado com sucesso.")
            else:
                self.__imprime_qualificadores(lista_qualificadores)
                inserindo = self.__tela.continuar("Qualificador nao foi criado: "
                                                  "valor inválido inserido em um dos campos.")
        if len(lista_qualificadores) != 0:
            return lista_qualificadores
        else:
            return None


# teste da classe controle
if __name__ == "__main__":
    ctrl = CtrlQualificador()
    ctrl.novo()
