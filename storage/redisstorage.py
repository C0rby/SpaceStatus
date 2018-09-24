from storage.storage import Storage
import redis
from datetime import datetime 

class RedisStorage(Storage):

  def __init__(self, config):
    self.redis = redis.Redis(host='localhost', port=6379)

  def store(self, key, value):
    now = datetime.now()
    entry = {
      key : value,
      key + ':time' : now
    }
    self.redis.hmset('spacestatus', entry)

  def entries(self):
    return self.redis.hgetall('spacestatus') 
    
