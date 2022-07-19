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

    def criador(self):
        titulo_qualificadores = self.__tela.menu_criacao()
        qualificadores = []

        if titulo_qualificadores is None:
            return None
        else:
            for titulo in titulo_qualificadores:
                qualificadores.append(Qualificador(titulo, ''))
                return qualificadores

    def novo(self, titulo: str, descricao: str):
        if isinstance(titulo, str) and isinstance(descricao, str):
            return Qualificador(titulo, descricao)
        else:
            return None




# teste da classe controle
if __name__ == "__main__":
    ctrl = CtrlQualificador()
    ctrl.criador()
