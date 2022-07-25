from entidade.pessoa_juridica import PessoaJuridica
from persistencia.DAO import DAO

class DAOPessoaJuridica(DAO):
    def __init__(self):
        super().__init__("data/data_pessoa_juridica.pkl")

    def add(self, objeto):
        if isinstance(objeto, PessoaJuridica) and isinstance(objeto.num_doc, int):
            super().add(objeto.num_doc, objeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
