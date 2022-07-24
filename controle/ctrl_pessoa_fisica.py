from controle.abstract_ctrl import AbstractCtrl
from entidade.pessoa_fisica import PessoaFisica
from visao.tela_pessoa_fisica import TelaPessoaFisica


class PessoaFisicaCtrl():
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaFisica()

    def signup(self):
        info = self.__tela.tela_signup_open()
        self.__tela.tela_close()
        if info == None:
            return None

        for usuario in self.__usuarios:
            if usuario.numDoc == info["num_doc"] or usuario.email == info["email"]:
                self.__tela.pop_up("Erro de cadastro repetido", "Usuario com esse CPF ou email ja cadastrado")
                break
        else:
            pessoa = PessoaFisica(info["nome"],info["num_doc"],info["email"])
            self.__usuarios.append(pessoa)

    def login(self):
        info = self.__tela.tela_login_open()
        self.__tela.tela_close()
        if info == None:
            return None

        for usuario in self.__usuarios:
            if str(usuario.numDoc) == info["num_doc"] and usuario.email == info["email"]:
                return(usuario)
        else:
            self.__tela.pop_up("Usuario nao cadastrado", "Nenhum usuario com essas credenciais encontrado")

    @property
    def usuarios(self):
        return self.__usuarios

    def set_todos_false(self):
        for usuario in self.__usuarios:
            usuario.cadastrouHoje = False
