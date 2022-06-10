from abc import ABC, abstractmethod


class AbstractCtrl(ABC):

  @abstractmethod
  def novo(self):
    pass
  
  @abstractmethod
  def busca(self):
    pass

  @abstractmethod
  def incluir(self):
    pass

  @abstractmethod
  def listar(self):
    pass

  @abstractmethod
  def alterar(self):
    pass

  @abstractmethod
  def excluir(self):
    pass
