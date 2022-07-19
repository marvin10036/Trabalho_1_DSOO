from visao.tela import Tela
from visao.tela_menu_basico import TelaMenuBasico
import PySimpleGUI as sg

class TelaPessoaJuridica(Tela):
    def __init__(self):
        self.__window = None

    def init_components_signup(self):
        sg.theme("DarkAmber")
        layout = [[sg.Text("Insira as informacoes do cadastro", size=(30,1),
                           font=("Arial", 15), justification="center")],
                  [sg.Text(" ")],
                  [sg.Text('Nome', size=(15, 1)), sg.InputText(key="nome")],
                  [sg.Text('Numero do documento', size=(15, 1)), sg.InputText(key="num_doc")],
                  [sg.Text('Email', size=(15, 1)), sg.InputText(key="email")],
                  [sg.Text(" ")],
                  [sg.Button("CONFIRMAR", size =(10,1)), sg.Text(" " * 35), sg.Button("CANCELAR", size =(10,1))]
                 ]
        self.__window = sg.Window("Signup").Layout(layout)

    def init_components_login(self):
        sg.theme("DarkAmber")
        layout = [[sg.Text("Insira as informacoes de login", size=(30,1),
                           font=("Arial", 15), justification="center")],
                  [sg.Text(" ")],
                  [sg.Text('Email', size=(15, 1)), sg.InputText(key="email")],
                  [sg.Text('Numero do CNPJ', size=(15, 1)), sg.InputText(key="num_doc")],
                  [sg.Text(" ")],
                  [sg.Button("CONFIRMAR", size =(10,1)), sg.Text(" " * 35), sg.Button("CANCELAR", size =(10,1))]
                 ]
        self.__window = sg.Window("Login").Layout(layout)

    def tela_signup_open(self):
        self.init_components_signup()
        button, values = self.__window.Read()
        if button == "CONFIRMAR":
            return values
        return None

    def tela_login_open(self):
        self.init_components_login()
        button, values = self.__window.Read()
        if button == "CONFIRMAR":
            return values
        return None

    def tela_close(self):
        self.__window.Close()

    def pop_up(self, titulo: str, msg: str):
        TelaMenuBasico().pop_up(titulo, msg)
