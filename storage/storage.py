from abc import ABC, abstractmethod

class Storage(ABC):

  @abstractmethod
  def store(self, key, value):
    pass

  @abstractmethod
  def entries(self):
   pass

