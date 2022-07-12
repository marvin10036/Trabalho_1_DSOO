from visao.tela import Tela
from visao.tela_menu_basico import TelaMenuBasico
import PySimpleGUI as sg

class TelaMercado(Tela):
    def __init__(self):
        self.__window = None
        self.__init_components()

    def __init_components(self):
        sg.theme('DarkAmber')

    def pede_nome(self):
        return super()._pede_str("Nome: ").capitalize()

    def pede_endereco(self):
        return super()._pede_str("Endereco: ").capitalize()

    def seleciona_mercado(self, n_de_mercados):
        return super()._seleciona_opcao_int(n_de_mercados)

    def pede_confirmacao(self):
        return super()._pergunta_sim_ou_nao("Tem certeza que deseja excluir essa opcao?")

    def open(self, opcoes: list):
        return TelaMenuBasico().open(opcoes, "Tela mercado")

    def pop_up(self, titulo: str, msg: str):
        TelaMenuBasico().pop_up(titulo, msg)