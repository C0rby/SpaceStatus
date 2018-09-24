from handler.handler import MessageHandler
import json


class TemperaturMessageHandler(MessageHandler):


  def __init__(self, storage):
    MessageHandler.__init__(self, storage)

  def topic(self):
    return "sensors/tischtennis/bricklet/temperature/tfj/temperature"

  def handle(self, client, userdata, message):
    payload = json.loads(message.payload)
    self.storage.store('temp', payload['temperature'] / 100)
