import socket
import threading
import sys

class Cliente():
    def __init__(self, host="localhost", port=7000):
        self.sock = socket.socket()
        self.sock.connect((host, port))

        mensajes_servidor = threading.Thread(target=self.mensaje_server)
        mensajes_servidor.daemon = True
        mensajes_servidor.start()

        while True:
            mensaje = input('=> ')
            if mensaje != 'salir':
                self.enviar_mensaje(mensaje)
            else:
                self.sock.close()
                sys.exit()

    def mensaje_server(self):
        while True:
            try:
                datos = self.sock.recv(1024)
                if datos:
                    print(datos.decode())
            except:
                pass

    def enviar_mensaje(self, mensaje):
        self.sock.send(mensaje.encode())

cliente = Cliente()