from controle.abstract_ctrl import AbstractCtrl
from visao.tela_pessoa_juridica import TelaPessoaJuridica
from entidade.pessoa_juridica import PessoaJuridica

class PessoaJuridicaCtrl(AbstractCtrl):
    def __init__(self):
        self.__usuarios = []
        self.__tela = TelaPessoaJuridica

    def signin(self):
        info = self.__tela().telaSignin()
        for usuario in self.__usuarios:
            if usuario.__numDoc == info["numDoc"] and usuario.__email == info["email"]:
                print("Usuario ja cadastrado")
                break
        else:
            pessoa = PessoaJuridica(info["nome"],info["numDoc"],info["email"])
            self.__usuarios.append(pessoa)
            return pessoa
       
    def login(self):
        info = self.__tela().telaLogin()
        for usuario in self.__usuarios:
            if usuario.numDoc == info["numDoc"] and usuario.email == info["email"]:
                return(usuario)
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


