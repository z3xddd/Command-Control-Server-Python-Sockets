#!/usr/bin/env python3

import socket
import time
import threading

HOST = '10.0.5.100'
PORT = 3334
SERVER = (HOST, PORT)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(SERVER)
servidor.listen(5)

def command_control():
    conexao, cliente = servidor.accept()
    print(f"Conectado, {cliente}")

    while True:
        print("Executando o Ping no cliente conectado.....")
        time.sleep(5)
        conexao.sendall("ping 8.8.8.8 -c 2".encode())
        time.sleep(5)
        print("Ping executado com sucesso.")
        time.sleep(5)
        conexao.close()
        break

thr1 = threading.Thread(name='Primeira-Conexao', target=command_control)
thr2 = threading.Thread(name='Segunda-Conexao', target=command_control)
thr3 = threading.Thread(name='Terceira-Conexao', target=command_control)

thr1.start()
thr2.start()
thr3.start()

servidor.close()