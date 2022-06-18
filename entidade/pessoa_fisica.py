from entidade.usuario import Usuario

class PessoaFisica(Usuario):
    def __init__(self, nome:str, numDoc:str, email:str):
        super(). __init__(nome,numDoc,email)

