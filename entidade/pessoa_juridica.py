from usuario import Usuario
from mercado import Mercado

class PessoaJuridica(Usuario):
    def __init__(self,nome:str,numDoc:str,email:str,estabelecimento:Mercado):
        super().__init__(self,nome,numDoc,email)
        self.__estabelecimento = estabelecimento

    @property
    def estabelecimento(self):
        return self.__estabelecimento

    @estabelecimento.setter
    def estabelecimento(self, new_estabelecimento):
        self.__establecimento = new_estabelecimento
        
