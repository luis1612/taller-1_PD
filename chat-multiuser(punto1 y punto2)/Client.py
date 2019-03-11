import socket
import threading
import sys
import pickle


class Cliente():
    """docstring for Cliente"""

    def __init__(self, nombre, host="127.0.0.1", port=9999):

        self.nombre = nombre
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.msg_recv)

        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('>')
            if msg != 'salir':
                self.send_msg((msg, self.nombre))
            else:
                self.send_msg((msg,self.nombre))
                self.sock.close()
                sys.exit()

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    mensaje, propietario = pickle.loads(data)
                    if mensaje != 'salir':
                        print(propietario,':',mensaje)
                    else:
                        print(propietario, 'ha dejado el chat')
            except:

                pass

    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))


nombre = input('Ingrese su nombre de usuario: ')
print('Bienvenido al chat', nombre)
c = Cliente(nombre)
