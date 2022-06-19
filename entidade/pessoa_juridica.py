from entidade.usuario import Usuario
from entidade.mercado import Mercado

class PessoaJuridica(Usuario):
    def __init__(self,nome:str,numDoc:int, email: str):
        super().__init__(nome,numDoc, email)
        self.__estabelecimento = None

    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @estabelecimento.setter
    def estabelecimento(self, new_estabelecimento):
        self.__establecimento = new_estabelecimento
        
