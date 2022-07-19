from controle.abstract_ctrl import AbstractCtrl
from entidade.pessoa_fisica import PessoaFisica
from visao.tela_pessoa_fisica import TelaPessoaFisica


class PessoaFisicaCtrl():
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaFisica()

    def signup(self):
        info = self.__tela.telaSignup()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] or usuario.email == info["email"]:
                self.__tela.imprime("Usuario com esse CPF ou email ja cadastrado")
                break
        else:
            pessoa = PessoaFisica(info["nome"],info["numDoc"],info["email"])
            self.__usuarios.append(pessoa)
            self.__tela.imprime("Cadastro realizado com sucesso")

    def login(self):
        info = self.__tela.telaLogin()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] and usuario.email == info["email"]:
                return (usuario)
        else:
            self.__tela.imprime("Usuario nao cadastrado")

    @property
    def usuarios(self):
        return self.__usuarios

    def set_todos_false(self):
        for usuario in self.__usuarios:
            usuario.cadastrouHoje = False

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
