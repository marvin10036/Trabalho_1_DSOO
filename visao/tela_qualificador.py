from visao.tela import Tela
import PySimpleGUI as sg


class TelaQualificador(Tela):

    def menu_criacao(self):
        titulo_qualificadores = []
        self.pop_up("Criacao de qualificadores para produto:",
                    "Insira o nome e clique em 'adicionar'. Ex: 'Peso'. Finalize em 'pronto'")
        while True:
            layout = [
                [sg.Text("Insira o nome do titulo", size=(30, 1), font=('Arial', 15))],
                [sg.Text('Titulo:', size=(15, 1)), sg.InputText()],
                [sg.Button("ADICIONAR"), sg.Button('PRONTO'), sg.Button('CANCELAR')]
            ]
            window = sg.Window('Edicao de dados', default_element_size=(40, 1)).Layout(layout)

            button, values = window.Read()
            value_list = list(values.values())
            window.Close()

            if button == 'ADICIONAR':
                if '' in value_list:
                    self.pop_up('Erro: campo vazio', 'Preencha todos os campos.')
                else:
                    titulo_qualificadores.append(value_list[0].capitalize())
                    self.pop_up("Qualificador adicionado.", "Continue inserindo ou clique em pronto.")
            elif button == 'PRONTO':
                if len(titulo_qualificadores) == 0:
                    self.pop_up('Nenhum qualificador inserido.', 'Operacao cancelada.')
                else:
                    for qualif in titulo_qualificadores:
                        print(qualif)
                    return titulo_qualificadores
            else:
                return None

    def pop_up(self, titulo: str, msg: str):
        sg.Popup(titulo, msg)

#teste para TelaQualificador
if __name__ == "__main__":
    print(TelaQualificador().menu_criacao())