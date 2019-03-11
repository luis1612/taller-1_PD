import socket
import threading
import sys

class Servidor():
    def __init__(self, host="localhost", port=7000):
        self.clientes = []
        self.sock = socket.socket()
        self.sock.bind((host, port))

        self.sock.listen(10)
        self.sock.setblocking(False)

        aceptar = threading.Thread(target=self.aceptarConexiones)
        procesar = threading.Thread(target=self.procesarConexiones)

        aceptar.daemon = True
        procesar.daemon = True
        aceptar.start()
        procesar.start()

        try:
            while True:
                mensaje = input('=> ')
                if mensaje == 'salir':
                    self.sock.close()
                    sys.exit()
        except:
            self.sock.close()
            sys.exit()

    def mensaje_todos(self, mensaje, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(mensaje)
            except:
                self.clientes.remove(c)

    def aceptarConexiones(self):
        print("Chat iniciado")
        while True:
            try:
                conexion, direccion = self.sock.accept()
                conexion.setblocking(False)
                self.clientes.append(conexion)
            except:
                pass

    def procesarConexiones(self):
        print("Procesar Conexion")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        datos = c.recv(1024)
                        if datos:
                            self.mensaje_todos(datos, c)
                    except:
                        pass

servidor = Servidor()