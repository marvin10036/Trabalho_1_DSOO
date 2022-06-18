from controle.ctrl_pessoa_juridica import PessoaJuridicaCtrl
from controle.ctrl_pessoa_fisica import PessoaFisicaCtrl
from visao.tela_usuario import TelaUsuario

class CtrlUsuario:
    def __init__(self):
        self.__tela = TelaUsuario()
        self.__pessoa_juridica_ctrl = PessoaJuridicaCtrl()
        self.__pessoa_fisica_ctrl = PessoaFisicaCtrl()

    def pede_tipo(self):
        switcher = {1:self.__pessoa_fisica_ctrl, 2:self.__pessoa_juridica_ctrl}
        opcao = self.__tela.pedeTipoUsuario()

        return (switcher[opcao])

    def signin(self):
        return self.pede_tipo().signin()

    def login(self):
        return self.pede_tipo().login()

    def retorna_tipo(self, usuario):
        tipostr = (str(type(usuario)))[33:-2]
        return tipostr
