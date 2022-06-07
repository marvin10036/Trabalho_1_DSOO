from abc import ABC, abstractmethod


class AbstractCtrl(ABC):
  
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
