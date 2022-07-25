from entidade.registro_de_preco import RegistroDePreco
from persistencia.DAO import DAO
import os


class DAORegistroDePreco(DAO):
    def __init__(self):
        super().__init__("data/data_registro_de_preco.pkl")

    def add(self, objeto, identifier):
        if isinstance(objeto, RegistroDePreco) and isinstance(identifier, int):
            super().add(identifier, objeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
