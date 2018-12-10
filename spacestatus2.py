#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from handler.handler import MessageHandler
from vendor import importdir
import paho.mqtt.client as paho
from storage.redisstorage import RedisStorage
import dataprovider
from multiprocessing import Process


def mqtt_client(config):
  """Creates a new mqtt client"""
  client = paho.Client('spacestatus2')
  client.username_pw_set('spacestatus2', 'password')
  return client

def con(client, userdata, flags, rc):
  mqtt_client.subscribe('sensors/#')

def msg(client, userdata, msg):
  #print('msg ' + str(msg.payload.decode('utf-8')))
  pass

if __name__ == '__main__':
  storage = RedisStorage(None)

  mqtt_client = mqtt_client(None)
  mqtt_client.on_connect = con
  mqtt_client.on_message = msg
  mqtt_client.clean_session = False
  #mqtt_client.connect('192.168.178.20', keepalive=60)

  importdir.do("handler", globals())
  handlers = [handler(storage) for handler in MessageHandler.__subclasses__()]
  for handler in handlers:
    print(handler.topic())
    mqtt_client.message_callback_add(handler.topic(), handler.handle)

  http_provider = dataprovider.HttpProvider(storage)

  try:
    p1 = Process(target=http_provider.run())
    p2 = Process(target=mqtt_client.loop_forever)
    p1.start()
    print('foo')  
    p2.start()
    print('bar')
  except:
    http_provider.stop()
