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

    def novo(self):
        inserindo = True
        lista_qualificadores = []

        self.__tela.imprime_titulo("Novo conjunto de qualificadores")
        while inserindo is True:
            titulo = self.__tela.pede_titulo()  #todo nao pode ter dois com mesmo titulo
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
            self.__tela.imprime_linha_de_fechamento()
            return lista_qualificadores
        else:
            self.__tela.imprime("[Qualificadores nao foram criados]")
            self.__tela.imprime_linha_de_fechamento()
            return None


# teste da classe controle
if __name__ == "__main__":
    ctrl = CtrlQualificador()
    ctrl.novo()
