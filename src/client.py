import subprocess
import xmlrpc.client
from os import system, name
import time
import threading
from config import *
import random
import os
import sys

def cls1():  #APENAS UMA SIMPLES FUNC PARA LIMPAR A TELA(clear)
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

nome = ""
temp_messages = []
proxy = xmlrpc.client.ServerProxy("http://{}:{}/".format(IP, PORT))
status = False

def check_messagens(proxy):
    global temp_messages
    global status
    while True:
        time.sleep(1)
        data = proxy.send_message_list()
        if data != temp_messages:
            for d in data:
                if d not in temp_messages:
                    temp_messages.append(d)
                    print(f"\n{d[:int(len(d)-4)]}")

def pergunta_por_message():
    while True:
        msg = input()
        if msg != "":
            id_of_message = random.randint(1000, 9999)
            messagens_totais = proxy.send_message(msg+str(id_of_message), nome)

def main():
    global nome
    cls1()
    print("Bem-Vindo ao Demo Chat Server 1.0\n\n")
    nome = input("Nome?: ")
    func = threading.Thread(target=check_messagens, args=(proxy,))
    func.start()
    while True:
        if status == False:
            pergunta_por_message()
            print(CURSOR_UP_ONE + ERASE_LINE + inp)

if __name__ == "__main__":
    print("A conectar ao servidor...")
    main()
