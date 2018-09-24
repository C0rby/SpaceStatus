from handler.handler import MessageHandler


class SoundMessageHandler(MessageHandler):


  def __init__(self, storage):
    MessageHandler.__init__(self, storage)

  def topic(self):
    return "sensors/tischtennis/bricklet/sound_intensity/voE/intensity"

  def handle(self, client, userdata, message):
    print('Sound ' + str(message.payload))
