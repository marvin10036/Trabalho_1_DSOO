from visao.tela import Tela
import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self):
        self.__window = None

    def pop_up(self, titulo: str, msg: str):
        sg.Popup(titulo, msg)

    def menu_principal(self):
        layout = [
            [sg.Text("Menu principal",
                     size=(30, 1), font=('Arial', 15), justification='c')],
            [sg.Button('1'), sg.Text('Novo registro de preco', size=(25, 1))],
            [sg.Button('2'), sg.Text('Buscar registro de preco', size=(25, 1))],
            [sg.Button('3'), sg.Text('Menus e dados', size=(25, 1))],
            [sg.Button('0'), sg.Text('Logoff', size=(25, 1))],
        ]
        window = sg.Window('Menu principal', default_element_size=(40, 1)).Layout(layout)

        button, values = window.Read()
        window.Close()

        if (button is None) or button == '0':
            return 0
        elif button == '1':
            return 1
        elif button == '2':
            return 2
        elif button == '3':
            return 3

    def menu_dados(self):
        layout = [
            [sg.Text("Menu dados",
                     size=(30, 1), font=('Arial', 15), justification='c')],
            [sg.Button('1'), sg.Text('Menu categoria', size=(25, 1))],
            [sg.Button('2'), sg.Text('Menu mercado', size=(25, 1))],
            [sg.Button('3'), sg.Text('Menu produto', size=(25, 1))],
            [sg.Button('4'), sg.Text('Menu registro', size=(25, 1))],
            [sg.Button('0'), sg.Text('Logoff', size=(25, 1))],
        ]
        window = sg.Window('Menu dados', default_element_size=(40, 1)).Layout(layout)

        button, values = window.Read()
        window.Close()

        if (button is None) or button == '0':
            return 0
        elif button == '1':
            return 1
        elif button == '2':
            return 2
        elif button == '3':
            return 3
        elif button == '4':
            return 4

    def opcoes_menu_principal(self) -> int:
        super().imprime_titulo("Menu principal")
        print("1 - Novo registro de preco")
        print("2 - Buscar registro de preco")
        print("3 - Editar dados do sistema")
        print("0 - Deslogar")
        return super()._seleciona_opcao_int(3)

    def pede_nome_produto(self):
        return super()._pede_str("Nome do produto: ")

    def pede_descricao_qualificador(self, titulo: str):
        return input(titulo)

    def pede_confirmacao(self, texto: str):
        return super()._pergunta_sim_ou_nao(texto)

    def opcoes_editar_dados(self):
        super().imprime_titulo("Menu editar dados")
        print("1 - Categorias")
        print("2 - Mercados")
        print("3 - Produtos")
        print("4 - Registros de preco")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(4)

    def opcoes_menu_registro(self):
        super().imprime_titulo("Menu Registro")
        print("1 - Listar registros")
        print("2 - Novo registro")
        print("3 - Excluir registro")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(3)

    def opcoes_menu_categoria(self):
        super().imprime_titulo("Menu Categoria")
        print("1 - Listar categorias")
        print("2 - Nova categoria")
        print("3 - Editar categoria")
        print("4 - Excluir categoria")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(4)

    def opcoes_menu_mercado(self):
        super().imprime_titulo("Menu Mercado")
        print("1 - Listar mercados")
        print("2 - Novo mercado")
        print("3 - Editar mercado")
        print("4 - Excluir mercado")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(4)

    def opcoes_menu_produto(self):
        super().imprime_titulo("Menu Produto")
        print("1 - Listar produtos")
        print("2 - Novo produto")
        print("3 - Editar produto")
        print("4 - Excluir produto")
        print("5 - Detalhes produto")
        print("0 - Voltar")
        return super()._seleciona_opcao_int(5)

    def init_components_menu_usuario(self):
        layout = [
            [sg.Text(" " * 80), sg.Button("Login", size=(7,1)), sg.Button("Signup",size=(7,1))],
            [sg.Text(" ")],
            [sg.Text(" ")],
            [sg.Text("Sistema legal",
                     size=(30, 1), font=('Arial', 22), justification='center')],
            [sg.Text(" ")],
            [sg.Text(" ")],
            [sg.Button('Avancar um dia', size=(18,1)), sg.Text(" " * 35), sg.Button('Fechar programa', size=(18,1))],
        ]
        self.__window = sg.Window('Inicio do Sistema', default_element_size=(40, 1)).Layout(layout)

    def menu_usuario_open(self):
        self.init_components_menu_usuario()
        button = self.__window.Read()
        if button[0] == None:
            return None
        switcher = {"Fechar programa":0, "Signup":1, "Login": 2, "Avancar um dia":3}
        return switcher[button[0]]

    def close(self):
        self.__window.Close()
