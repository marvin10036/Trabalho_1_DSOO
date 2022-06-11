from entidade.qualificador import Qualificador
from visao.tela_qualificador import TelaQualificador


class CtrlQualificador():
    def __init__(self):
        self.__tela = TelaQualificador()

    def __imprime_qualificadores(self, qualificadores: list):
        self.__tela.imprimeTitulo("Qualificadores")
        for qualificador in qualificadores:
            titulo = qualificador.titulo
            descricao = qualificador.descricao
            self.__tela.imprimeQualificador(titulo, descricao)
        self.__tela.linhaDeFechamento()

    def novo(self) -> list:
        inserindo = True
        listaQualificadores = []

        while (inserindo == True):
            titulo = self.__tela.pedeTitulo()
            descricao = self.__tela.pedeDescricao()

            if (titulo != None) and (descricao != None):
                listaQualificadores.append(Qualificador(titulo, descricao))
                self.__imprime_qualificadores(listaQualificadores)
                inserindo = self.__tela.continuar("Qualificador criado com sucesso.")
            else:
                self.__imprime_qualificadores(listaQualificadores)
                inserindo = self.__tela.continuar("Qualificador nao foi criado: "
                                                  "valor inválido inserido em um dos campos.")
        if len(listaQualificadores) != 0:
            return listaQualificadores
        else:
            return None


#teste da classe controle
if __name__ == "__main__":
    ctrl = CtrlQualificador()
    ctrl.novo()