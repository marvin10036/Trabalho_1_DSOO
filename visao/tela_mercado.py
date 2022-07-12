from visao.tela import Tela
from visao.tela_seleciona_da_lista import TelaSelecionaDaLista
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

    def seleciona_opcao(self, opcoes: list):
        tela = TelaSelecionaDaLista()
        return tela.seleciona_opcao_int(opcoes, "Selecionar mercado")

class TelaMercadoComGui():
    def __init__(self):
        self.__window = None
        self.__init_components()

    def __init_components(self):
        sg.theme('DarkAmber')

    def __atualiza_layout(self, opcoes=[]):
        layout = [
            [sg.Text('Selecione uma opcao da lista', size=(30, 1), font=('Arial', 20))],
            [sg.Listbox(values=opcoes, size=(70, 5), key='lb_itens'),
             sg.Button('OK')]
        ]
        return layout

    def __atualiza_opcoes(self, opcoes):
        layout = self.__atualiza_layout(opcoes)
        self.__window = sg.Window('Selecionar opcao', default_element_size=(40, 1)).Layout(layout)

    def open(self, opcoes=[]):
        self.__atualiza_opcoes(opcoes)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()