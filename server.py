#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
	"""
	Echo server class
	"""
    #Diccionario como atributo de clase
	Users = {}
			
	def handle(self):
		self.wfile.write(b"SIP/2.0 200 OK")
		print("Nuevo cliente IP y puerto:", self.client_address)  
		Line = self.rfile.read().decode('utf-8')
		print("El cliente nos manda ", Line)
		Expires = int(Line.split(' ')[3].split('\r')[0])
		Expires_Time = time.strftime('%Y-%m-%d %H:%M:%S', 
									 time.gmtime(time.time() + Expires))
		if Line.split(' ')[0] == 'REGISTER':
			Addres = Line.split(' ')[1]
			Addres = Addres.split(':')[1]
			print(Line.split(' ')[3])
			self.Users[Addres] = {'IP': self.client_address[0], 
								  'Expires': Expires_Time}
		if Expires == '0':
			del self.Users[Addres]
		print(self.Users)
		#creamos una lista con los usuarios a borrar
		self.register2json()
		Expire_List = self.deleteUsers()
	
		for name in Expire_List:
			del self.Users[name]
		
	def register2json(self):
		with open('registered.json', 'w') as Fich_Users:
			json.dump(self.Users, Fich_Users, sort_keys=True, indent='\t',
					  separators=(',', ':'))
					  
	def deleteUsers(self):
		Now = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
		To_Delete = []
		for name in self.Users:
			if self.Users[name]['Expires'] < Now:
				To_Delete.append(name)
		return To_Delete
				 

#Puerto del server            
Port = int(sys.argv[1])

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', Port), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
