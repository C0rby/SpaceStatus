from handler.handler import MessageHandler
import json


class DoorMessageHandler(MessageHandler):

  def __init__(self, storage):
    MessageHandler.__init__(self, storage)

  def topic(self):
    return 'sensors/door/default/status'

  def handle(self, client, userdata, message):
    payload = json.loads(message.payload)
    self.storage.store('door', payload['value'])
