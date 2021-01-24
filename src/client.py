import subprocess
import xmlrpc.client
from os import system, name
import time
import threading
from config import *
import os
import sys

def cls1():  #APENAS UMA SIMPLES FUNC PARA LIMPAR A TELA(clear)
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

nome = ""
proxy = xmlrpc.client.ServerProxy("http://{}:{}/".format(IP, PORT))

def pergunta_por_message():
    while True:
        msg = input(">>> ")
        if msg != "":
            messagens_totais = proxy.send_message(msg, nome)
            cls1()

def main():
    global nome
    cls1()
    print("Bem-Vindo ao Demo Chat Server 1.0\n\n")
    nome = input("Nome?: ")
    os.system(f"start cmd /k {sys.executable} utils.py")
    func = threading.Thread(target=pergunta_por_message)
    func.start()

if __name__ == "__main__":
    print("A conectar ao servidor...")
    main()