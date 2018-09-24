from handler.handler import MessageHandler


class DoorMessageHandler(MessageHandler):

  def __init__(self, storage):
    MessageHandler.__init__(self, storage)

  def topic(self):
    return 'sensors/door/default/status'

  def handle(self, client, userdata, message):
    print('Door ' + str(message.payload.decode('utf-8')))
  
