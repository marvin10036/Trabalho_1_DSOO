from visao.tela import Tela
import PySimpleGUI as sg
from visao.tela_menu_basico import TelaMenuBasico


class TelaRegistroDePreco(Tela):
    def __init__(self):
        self.__window = None

    def seleciona_opcao_lista(self, n_de_opcoes):
        return super()._seleciona_opcao_int(n_de_opcoes)

    def pede_confirmacao(self):
        return super()._pergunta_sim_ou_nao("Tem certeza que deseja excluir a opcao selecionada?")

    def init_components_opcoes_iniciais(self):
        sg.theme("DarkAmber")
        layout = [[sg.Text("Menu de busca", size=(30,1),
                           font=("Arial", 15), justification="center")],
                  [sg.Text(" ")],
                  [sg.Text("Escreva o produto que quer buscar.")],
                  [sg.Text("Eh permitido a insercao de apenas um qualificador por vez separado por espaco:")],
                  [sg.InputText(key="texto")],
                  [sg.Text(" ")],
                  [sg.Button("PESQUISAR", size =(10,1)), sg.Text(" " * 35), sg.Button("CANCELAR", size =(10,1))]
                 ]
        self.__window = sg.Window("Menu de busca").Layout(layout)

    def opcoes_iniciais_open(self):
        self.init_components_opcoes_iniciais()
        button, values = self.__window.Read()
        print(values)
        if button == "PESQUISAR":
            return values["texto"]
        return None

    def init_components_opcao_ordenacao(self):
        layout = [
            [sg.Text("Escolha a opcao de ordenacao",
                     size=(30, 1), font=('Arial', 15), justification='center')],
            [sg.Button('1'), sg.Text('Nenhuma', size=(25, 1))],
            [sg.Button('2'), sg.Text('Preco', size=(25, 1))],
            [sg.Button('3'), sg.Text('Numero de confirmacoes', size=(25, 1))],
            [sg.Button('4'), sg.Text('Data de postagem', size=(25, 1))],
            [sg.Button('0'), sg.Text('Cancelar', size=(25, 1))]
        ]
        self.__window = sg.Window('Filtro', default_element_size=(40, 1)).Layout(layout)

    def opcao_ordenacao_open(self):
        self.init_components_opcao_ordenacao()
        button, values = self.__window.Read()
        print(button)
        return int(button)

    def init_components_printar_lista(self, matriz):
        sg.theme("DarkAmber")
        headings = ["Produto", "Qualificadores", "Mercado", "Preco", "Confirmacoes", "Data"]

        layout = [
            [sg.Table(values=matriz,
                      headings=headings,
                      max_col_width=35,
                      auto_size_columns=True,
                      justification='right',
                      num_rows=10,
                      key='tabela',
                      row_height=35)],
            [sg.Text(" ")],
            [sg.Text(" " * 35), sg.Button("SAIR", size =(10,1))]
        ]
        self.__window = sg.Window("Registros de produtos").Layout(layout)

    def printar_lista_open(self, matriz):
        self.init_components_printar_lista(matriz)
        button, values = self.__window.Read()

        return None

    def tela_close(self):
        self.__window.Close()

    def pop_up(self, titulo: str, msg: str):
        TelaMenuBasico().pop_up(titulo, msg)