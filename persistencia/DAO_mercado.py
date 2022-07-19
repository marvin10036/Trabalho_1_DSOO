from persistencia.DAO import DAO
from entidade.mercado import Mercado

class DAOMercado(DAO):
    def __init__(self):
        super().__init__("../persistencia/data/data_mercado.pkl")

    def add(self, objeto): #TODO adaptar tipo conforme necessario
        if isinstance(objeto, Mercado) and isinstance(objeto.nome, str):
            super().add(objeto.nome, objeto)

    def get(self, key: str): #TODO adaptar tipo conforme necessario
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str): #TODO adaptar tipo conforme necessario
        if isinstance(key, str):
            return super().remove(key)


if __name__ == "__main__":
    dao = DAOMercado()