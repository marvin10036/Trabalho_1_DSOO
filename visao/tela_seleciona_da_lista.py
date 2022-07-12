import PySimpleGUI as sg

class TelaSelecionaDaLista():
    def __init__(self):
        self.__window = None
        sg.theme('DarkAmber')

    def seleciona_opcao_int(self, opcoes=[], nome_janela='Selecionar opcao'):
        #cria layout
        layout = [
            [sg.Text('Selecione uma opcao da lista.', size=(30, 1), font=('Arial', 20))],
            [sg.Listbox(values=opcoes, size=(70, 5), key='lb_itens')],
            [sg.Button('OK'), sg.Button('NOVO')]
        ]
        self.__window = sg.Window(nome_janela, default_element_size=(40, 1)).Layout(layout)

        #le os botoes
        button, values = self.__window.Read()
        self.__window.Close()

        #processa os botoes/valores lidos
        if button == 'OK':
            valor = values['lb_itens']
            if len(valor) != 0:
                return valor[0][0]
        elif button == 'NOVO':
            return '0'
        else:
            return None