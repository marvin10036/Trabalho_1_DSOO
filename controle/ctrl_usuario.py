from controle.ctrl_pessoa_juridica import PessoaJuridicaCtrl
from controle.ctrl_pessoa_fisica import PessoaFisicaCtrl
from visao.tela_usuario import TelaUsuario

class CtrlUsuario:
    def __init__(self):
        self.__tela = TelaUsuario()
        self.__pessoa_juridica_ctrl = PessoaJuridicaCtrl()
        self.__pessoa_fisica_ctrl = PessoaFisicaCtrl()

    def pede_tipo(self):
        switcher = {0:None, 1:self.__pessoa_fisica_ctrl, 2:self.__pessoa_juridica_ctrl}
        opcao = self.__tela.open()
        self.__tela.close()

        return (switcher[opcao])

    def signup(self):
        opcao = self.pede_tipo()
        if opcao == None:
            return opcao
        return opcao.signup()

    def login(self):
        opcao = self.pede_tipo()
        if opcao == None:
            return opcao
        return opcao.login()

    def retorna_tipo(self, usuario):
        tipostr = (str(type(usuario)))[33:-2]
        return tipostr

    def setta_cadastrou_usuarios(self):
        self.__pessoa_juridica_ctrl.set_todos_false()
        self.__pessoa_fisica_ctrl.set_todos_false()