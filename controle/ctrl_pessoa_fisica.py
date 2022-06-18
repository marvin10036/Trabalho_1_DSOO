from controle.abstract_ctrl import AbstractCtrl
from entidade.pessoa_fisica import PessoaFisica
from visao.tela_pessoa_fisica import TelaPessoaFisica


class PessoaFisicaCtrl(AbstractCtrl):
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaFisica

    def signin(self):
        info = self.__tela().telaSignin()
        self.__usuarios.append(PessoaFisica(info["nome"], info["numDoc"], info["email"]))

    def login(self):
        info = self.__tela().telaLogin()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] and usuario.email == info["email"]:
                return (usuario)
        else:
            print("Usuario nao cadastrado")

    def criador(self):
        pass

    def novo(self):
        pass

    def busca(self):
        pass

    def incluir(self):
        pass

    def listar(self):
        pass

    def alterar(self):
        pass

    def excluir(self):
        pass
