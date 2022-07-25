from entidade.registro_de_preco import RegistroDePreco
from persistencia.DAO import DAO
import os


class DAORegistroDePreco(DAO):
    def __init__(self):
        caminho = os.getcwd()
        caminho = os.path.join(caminho, "controle/data/data_registro_de_preco.pkl")

        super().__init__(caminho)

    def add(self, objeto, identifier):
        if isinstance(objeto, RegistroDePreco) and isinstance(identifier, int):
            super().add(identifier, objeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
