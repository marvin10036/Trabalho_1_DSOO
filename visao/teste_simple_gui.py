import PySimpleGUI as sg

class Tela():
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

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

if __name__ == "__main__":
    tela = Tela()
    opcoes = ['opcao 1', 'opcao 2']
    button, values = tela.open(opcoes)
    print(button)
    print(values)
    tela.close()
    opcoes = ['opcao 1', 'opcao 2']
    button, values = tela.open(opcoes)
    print(button)
    print(values)
    tela.close()