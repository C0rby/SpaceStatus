from handler.handler import MessageHandler
import json


class UvMessageHandler(MessageHandler):


  def __init__(self, storage):
    MessageHandler.__init__(self, storage)

  def topic(self):
    return "sensors/tischtennis/bricklet/uv_light/xpa/uv_light"

  def handle(self, client, userdata, message):
    payload = json.loads(message.payload)
    self.storage.store('uv', payload['uv_light'])
