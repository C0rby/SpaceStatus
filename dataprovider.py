from http.server import BaseHTTPRequestHandler
import socketserver
import storage


class SpaceStatusHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    try:
      entries = self.server.storage.entries()
    except:
      # handle error
      return

    content = bytes(str(entries), 'utf-8')
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(content)
    return
     
class HttpProvider:

  def __init__(self, storage, config={'port':8081}):
    self.server = socketserver.TCPServer(('',config['port']), SpaceStatusHandler)
    self.server.storage = storage

  def run(self):
    self.server.serve_forever()

  def stop(self):
    self.server.socket.close()
