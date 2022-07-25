from entidade.usuario import Usuario

class PessoaFisica(Usuario):
    def __init__(self, nome:str, num_doc:int, email:str):
        super().__init__(nome,num_doc,email)
