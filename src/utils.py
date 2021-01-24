import subprocess
import sys
import xmlrpc.client
from os import system, name
import time
import threading
from config import *

temp_messages = []
proxy = xmlrpc.client.ServerProxy("http://{}:{}/".format(IP, PORT))

def cls():  #APENAS UMA SIMPLES FUNC PARA LIMPAR A TELA(clear)
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')
        
def check_messagens(proxy):
    while True:
        time.sleep(1)
        data = proxy.send_message_list()
        if data != temp_messages:
            cls()
            print("Chat em tempo real...\n\n")
            for d in data:
                print(d)

def main():
    cls()
    print("Bem-Vindo ao Demo Chat Server 1.0\n\n")
    func = threading.Thread(target=check_messagens, args=(proxy,))
    func.start()

if __name__ == "__main__":
    print("A conectar ao servidor...")
    main()