#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Dirección IP del servidor y contenido a enviar
try:
    Server = sys.argv[1]
    Port = int(sys.argv[2])
    Line = ' '.join(sys.argv[3:])
    Addres = sys.argv[4]
    Expires = sys.argv[5]
    if not str.isdigit(Expires):
        raise IndexError
except IndexError:
    print("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
if __name__ == "__main__":
    """Se crea socket y se manda register al servidor""""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((Server, Port))
        if sys.argv[3] == 'register':
            Line = ('REGISTER sip:' + Addres + ' SIP/2.0\r\n' +
                    'Expires: ' + Expires + '\r\n\r\n')
        else:
            sys.exit("Argumentos: ip puerto register sip_addres expires_value")
        print("Enviando:", Line)
        my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
        print("Socket terminado.")
