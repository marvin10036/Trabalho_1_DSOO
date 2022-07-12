import PySimpleGUI as sg

class TelaMenuBasico():
    def __init__(self):
        sg.theme('DarkAmber')

    def open(self, opcoes=[], nome_janela='Selecionar opcao', titulo='Selecione uma opcao da lista'):
        #cria layout
        coluna = [
            [sg.Button('NOVO')],
            [sg.Button('EDITAR')],
            [sg.Button('EXCLUIR')]
        ]
        layout = [
            [sg.Text(titulo, size=(30, 1), font=('Arial', 20), justification='c')],
            [sg.Listbox(values=opcoes, size=(70, 5), key='lb_itens'), sg.Column(coluna)],
            [sg.Button('SELECIONAR'),
             sg.Button('CANCELAR')
             ]
        ]
        window = sg.Window(nome_janela, default_element_size=(40, 1)).Layout(layout)

        #le os botoes
        button, values = window.Read()
        valor = values['lb_itens']

        foi_selecionado = False
        opcao_selecionada = None
        if valor is not None:
            if len(valor) != 0:
                foi_selecionado = True
                opcao_selecionada = int(valor[0][0]) - 1

        window.Close()
        return button, opcao_selecionada

    def pop_up(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)