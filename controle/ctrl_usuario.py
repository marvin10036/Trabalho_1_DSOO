from controle.ctrl_pessoa_juridica import PessoaJuridicaCtrl
from controle.ctrl_pessoa_fisica import PessoaFisicaCtrl
from visao.tela_usuario import TelaUsuario

class CtrlUsuario:
    def __init__(self):
        self.__tela = TelaUsuario()
        self.__pessoa_juridica_ctrl = PessoaJuridicaCtrl()
        self.__pessoa_fisica_ctrl = PessoaFisicaCtrl()

    def pedetipo(self):
        switcher = {1:self.__pessoa_fisica_ctrl, 2:self.__pessoa_juridica_ctrl}
        opcao = self.__tela.pedeTipoUsuario()

        return (switcher[opcao])

    def signin(self):
        self.pedetipo().signin()

    def login(self):
        self.pedetipo().login()
