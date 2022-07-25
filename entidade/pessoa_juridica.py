from entidade.usuario import Usuario
from entidade.mercado import Mercado

class PessoaJuridica(Usuario):
    def __init__(self,nome:str,num_doc:int, email: str):
        super().__init__(nome,num_doc, email)
        self.__estabelecimento = None

    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @estabelecimento.setter
    def estabelecimento(self, new_estabelecimento):
        self.__estabelecimento = new_estabelecimento
