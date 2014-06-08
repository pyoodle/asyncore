# Example of the asyncore server I'll be using -

import asyncore, socket

class server(asyncore.dispatcher):
  def __init__(self, address, port):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.set_reuse_addr()
    self.bind((address, port))
    self.listen(5)
  
  def accept(self):
    acception = self.accept()
    
    if acception is not None:
      connection, address = acception
      # Remember to write the chat logger
      handler = handle(connection)

class handle(asyncore.dispatcher_with_send):
  def read(self):
    data = self.recv(8192)
    
    if data is not None:
      # Uses the chat logger again
