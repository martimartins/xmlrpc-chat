from xmlrpc.server import SimpleXMLRPCServer
from config import *

class chat_server:
    def __init__(self, arg):
        self.arg = arg
        self.messagens = []

    def send_message(self, msg, author):
        if msg != "":
            self.messagens.append("[{}] - {}".format(author, msg))
            return self.messagens

    def send_message_list(self):
        return self.messagens

server = SimpleXMLRPCServer((IP, PORT))
print(f"Conexões abertas na port {IP}:{PORT}...\n")
server.register_instance(chat_server("a"))
print("Server pronto para receber messagens...")
server.serve_forever()