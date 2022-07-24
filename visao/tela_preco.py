import PySimpleGUI as sg


class TelaPreco():
    def menu_criacao(self):
        while True:
            layout = [
                [sg.Text("Insira o preco visto.", size=(30, 1), font=('Arial', 15))],
                [sg.Text('R$', size=(15, 1)), sg.InputText()],
                [sg.Button('PRONTO'), sg.Button('CANCELAR')]
            ]
            window = sg.Window('Inserir preco', default_element_size=(40, 1)).Layout(layout)

            button, values = window.Read()
            value_list = list(values.values())
            window.Close()

            if button == 'PRONTO':
                if '' in value_list:
                    self.pop_up('Erro: campo vazio', 'Preencha todos os campos.')
                else:
                    entrada = value_list[0].replace(",", ".")
                    try:
                        preco = round(float(entrada), 2)
                        return preco
                    except ValueError:  # ValueError
                        self.pop_up("Valor de entrada invalido:", "Tente novamente.")
            else:
                return None

    def pop_up(self, titulo, descricao):
        sg.Popup(titulo, descricao)