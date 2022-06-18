from abc import ABC

class Usuario(ABC):
    def __init__(self, nome:str, numDoc:int, email:str):
        self.__nome = nome
        self.__numDoc = numDoc
        self.__email = email
        self.__cadastrouHoje = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_nome:str):
        self.__nome = new_nome

    @property
    def numDoc(self):
        return self.__numDoc

    @numDoc.setter
    def numDoc(self, new_numDoc:int):
        self.__numDoc = new_numDoc

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email:str):
        self.__email = new_email

    @property
    def cadastrouHoje(self):
        return self.__cadastrouHoje

    @cadastrouHoje.setter
    def cadastrouHoje(self, new_cadastrouHoje:bool):
        self.__cadastrouHoje = new_cadastrouHoje



