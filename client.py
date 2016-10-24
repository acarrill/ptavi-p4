#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Dirección IP del servidor y contenido a enviar
Server = sys.argv[1]
Port = int(sys.argv[2])
Line = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
if __name__ == "__main__":
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
		my_socket.connect((Server, Port))
		print("Enviando:", Line)
		if sys.argv[3] == 'register':
			Line = 'REGISTER sip:' + sys.argv[4] + ' SIP/2.0\r\n\r\n'
		else:
			sys.exit('Forma de ejecutar cliente: ip puerto register usuario')
		my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
		data = my_socket.recv(1024)
		print('Recibido -- ', data.decode('utf-8'))
		print("Socket terminado.")
