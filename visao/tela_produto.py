from visao.tela import Tela
from visao.tela_menu_basico import TelaMenuBasico
import PySimpleGUI as sg

class TelaProduto(Tela):

    def menu_opcoes(self, opcoes: list):
        return TelaMenuBasico().open(opcoes, "Tela produto", "Menu produto")

    def menu_criacao(self, titulo: str):
        while True:
            layout = [
                [sg.Text(titulo,
                         size=(30, 1), font=('Arial', 15))],
                [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                [sg.Text('Descricao', size=(15, 1)), sg.InputText()],
                [sg.Button('PRONTO'), sg.Button('CANCELAR')]
            ]
            window = sg.Window('Edicao de dados', default_element_size=(40, 1)).Layout(layout)

            button, values = window.Read()
            value_list = list(values.values())
            window.Close()

            if button == 'PRONTO':
                if '' in value_list:
                    self.pop_up('Erro: campo vazio', 'Preencha todos os campos.')
                else:
                    return value_list
            else:
                return None

    def preencher_qualificadores(self, qualificadores: list):
        while True:
            qualif_preenchidos = []
            count = 0
            for qualificador in qualificadores:
                count += 1
                layout = [
                    [sg.Text("Preencha o qualificador {}".format(count), size=(30, 1), font=('Arial', 15))],
                    [sg.Text(qualificador, size=(15, 1)), sg.InputText()],
                    [sg.Button('PRONTO'), sg.Button('CANCELAR')]
                ]
                window = sg.Window('Preencher qualificadores', default_element_size=(40, 1)).Layout(layout)

                button, values = window.Read()
                value_list = list(values.values())
                window.Close()

                if button == 'PRONTO':
                    if '' in value_list:
                        self.pop_up('Erro: campo vazio', 'Preencha todos os campos.')
                    else:
                        qualif_preenchidos.append(value_list[0])
                else:
                    return None
            return qualif_preenchidos

    def pop_up(self, titulo: str, msg: str):
        TelaMenuBasico().pop_up(titulo, msg)

if __name__ == "__main__":
    preencher = ["marca", "peso"]
    valores = TelaProduto().preencher_qualificadores(preencher)
    print(valores)