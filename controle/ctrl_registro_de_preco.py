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
            self.__tela.printar_lista_completa(self.__registros)

if __name__ == "__main__":
    ctrl = CtrlRegistroDePreco()
