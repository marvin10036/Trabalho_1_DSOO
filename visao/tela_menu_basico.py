import PySimpleGUI as sg

class TelaMenuBasico():
    def __init__(self):
        sg.theme('DarkAmber')

    def open(self, opcoes=[], nome_janela='Selecionar opcao'):
        #cria layout
        coluna = [
            [sg.Button('NOVO')],
            [sg.Button('EDITAR')],
            [sg.Button('DELETAR')]
        ]
        layout = [
            [sg.Text('Selecione uma opcao da lista.', size=(30, 1), font=('Arial', 20), justification='c')],
            [sg.Listbox(values=opcoes, size=(70, 5), key='lb_itens'), sg.Column(coluna)],
            [sg.Button('SELECIONAR'),
             sg.Button('CANCELAR')
             ]
        ]
        window = sg.Window(nome_janela, default_element_size=(40, 1)).Layout(layout)

        #le os botoes
        button, values = window.Read()
        window.Close()
        return button, values