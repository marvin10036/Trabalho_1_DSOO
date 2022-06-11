from controle.ctrl_registro_de_preco import CtrlRegistroDePreco


class CtrlSistema():
    def __init__(self):
        self.__tela = None
        self.__ctrl_registro = CtrlRegistroDePreco()

    def programa_principal(self):
        print("Chamou programa principal.")


if __name__ == "__main__":
    CtrlSistema().programa_principal()