from visao.tela import Tela
import PySimpleGUI as sg

class TelaUsuario(Tela):
    def __init__(self):
        self.__window = None

    def pedeTipoUsuario(self):
        print("Escolha o tipo de pessoa: \n1 - Pessoa Fisica \n2 - Pessoa Juridica\n")
        opcao = self._seleciona_opcao_int(2)
        super().imprime_linha_de_fechamento()
        return(opcao)

    def init_components(self):
        sg.theme("DarkAmber")
        layout = [[sg.Text("Escolha o tipo de usuario", size=(30,1),
                           font=("Arial", 15), justification="center")],
                  [sg.Text(" ")],
                  [sg.Text(" " * 10), sg.Button("Pessoa Fisica", size=(8,3)), sg.Text(" " * 10),
                   sg.Button("Pessoa Juridica", size=(8,3))],
                  [sg.Text(" ")],
                  [sg.Text(" " * 45), sg.Button("CANCELAR", size =(10,1))]
                 ]
        self.__window = sg.Window("Tipo de Usuario").Layout(layout)

    def open(self):
        self.init_components()
        button = self.__window.Read()
        switcher = {"CANCELAR":0, "Pessoa Fisica":1, "Pessoa Juridica": 2}
        return switcher[button[0]]

    def close(self):
        self.__window.Close()
