#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
	"""
	Echo server class
	"""
    #Diccionario como atributo de clase
	Users = {}
	
	def handle(self):
		self.wfile.write(b"SIP/2.0 200 OK")
		print("Nuevo cliente IP y puerto:", self.client_address)  
		Line_Str = self.rfile.read().decode('utf-8')
		print("El cliente nos manda ", Line_Str)
		Expires = Line_Str.split(' ')[3].split('\r')[0]
		if Line_Str.split(' ')[0] == 'REGISTER':
			Addres = Line_Str.split(' ')[1]
			Addres = Addres.split(':')[1]
			print(Line_Str.split(' ')[3])
			self.Users[Addres] = {'IP': self.client_address[0], 
								  'Expires': Expires}
		if Expires == '0':
			del self.Users[Addres]
		print(self.Users)

#Puerto del server            
Port = int(sys.argv[1])

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', Port), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
