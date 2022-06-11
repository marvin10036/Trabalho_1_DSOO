
class Qualificador():
    def __init__(self, titulo: str, descricao: str):
        self.__titulo = titulo
        self.__descricao = descricao

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descricao(self):
        return self.__descricao

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
