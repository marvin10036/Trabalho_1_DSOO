from controle.abstract_ctrl import AbstractCtrl
from visao.tela_pessoa_juridica import TelaPessoaJuridica
from entidade.pessoa_juridica import PessoaJuridica

class PessoaJuridicaCtrl(AbstractCtrl):
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaJuridica()

    def signup(self):
        info = self.__tela.telaSignup()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] or usuario.email == info["email"]:
                self.__tela.imprime_titulo("Usuario com esse CNPJ ou email ja cadastrado")
                break
        else:
            pessoa = PessoaJuridica(info["nome"],info["numDoc"],info["email"])
            self.__usuarios.append(pessoa)
            return pessoa
       
    def login(self):
        info = self.__tela.telaLogin()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] and usuario.email == info["email"]:
                return(usuario)
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


