from abc import ABC, abstractmethod

class MessageHandler(ABC):

  @abstractmethod
  def __init__(self, storage):
    self.storage = storage

  @abstractmethod
  def topic(self):
    pass

  @abstractmethod
  def handle(self, client, userdata, message):
    pass
