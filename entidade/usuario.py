from abc import ABC

class Usuario(ABC):
    def __init__(self, nome:str, num_doc:int, email:str):
        self.__nome = nome
        self.__num_doc = num_doc
        self.__email = email
        self.__cadastrou_hoje = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_nome:str):
        self.__nome = new_nome

    @property
    def num_doc(self):
        return self.__num_doc

    @num_doc.setter
    def num_doc(self, new_num_doc:int):
        self.__num_doc = new_num_doc

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email:str):
        self.__email = new_email

    @property
    def cadastrou_hoje(self):
        return self.__cadastrou_hoje

    @cadastrou_hoje.setter
    def cadastrou_hoje(self, new_cadastrou_hoje:bool):
        self.__cadastrou_hoje = new_cadastrou_hoje
