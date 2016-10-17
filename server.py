#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        print("Nuevo cliente IP y puerto:", self.client_address)  
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))

#Puerto del server            
Port = int(sys.argv[1])

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', Port), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
