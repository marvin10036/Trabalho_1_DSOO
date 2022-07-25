from entidade.pessoa_juridica import PessoaJuridica
from persistencia.DAO import DAO
import os

class DAOPessoaJuridica(DAO):
    def __init__(self):
        super().__init__("data/data_pessoa_juridica.pkl")

    def add(self, objeto):
        if isinstance(objeto, PessoaJuridica) and isinstance(objeto.numDoc, int):
            super().add(objeto.numDoc, objeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
