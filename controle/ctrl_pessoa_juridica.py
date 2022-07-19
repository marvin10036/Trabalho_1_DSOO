from visao.tela_pessoa_juridica import TelaPessoaJuridica
from entidade.pessoa_juridica import PessoaJuridica


class PessoaJuridicaCtrl:
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaJuridica()

    def signup(self):
        info = self.__tela.tela_signup_open()
        self.__tela.tela_close()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["num_doc"] or usuario.email == info["email"]:
                self.__tela.pop_up("Erro de cadastro repetido", "Usuario com esse CNPJ ou email ja cadastrado")
                break
        else:
            pessoa = PessoaJuridica(info["nome"],info["num_doc"],info["email"])
            self.__usuarios.append(pessoa)
            return pessoa
       
    def login(self):
        info = self.__tela.tela_login_open()
        self.__tela.tela_close()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["num_doc"] and usuario.email == info["email"]:
                return(usuario)
        else:
            self.__tela.pop_up("Usuario nao cadastrado", "Nenhum usuario com essas credenciais encontrado")

    @property
    def usuarios(self):
        return self.__usuarios

    def set_todos_false(self):
        for usuario in self.__usuarios:
            usuario.cadastrouHoje = False
