from entidade.pessoa_fisica import PessoaFisica
from persistencia.DAO import DAO
import os

class DAOPessoaFisica(DAO):
    def __init__(self):
        super().__init__("data/data_pessoa_fisica.pkl")

    def add(self, objeto):
        if isinstance(objeto, PessoaFisica) and isinstance(objeto.numDoc, int):
            super().add(objeto.numDoc, objeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
