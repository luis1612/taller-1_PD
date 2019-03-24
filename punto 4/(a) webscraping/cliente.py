import threading
import socket
import sys

class Cliente():
    def __init__(self, host="localhost", port=8999):
        self.sock = socket.socket()
        self.sock.connect((host, port))

        menj_sv = threading.Thread(target=self.mj_sv)
        menj_sv.setDaemon = True
        menj_sv.start()

        url = input("seleccione:\n"
                        "a. BOOKING.COM Alojamiento - Webscraping .\n"
                        "b. Salir.\n"
                 "Escoja una: ")

        while True:
            self.mandarmensj(url)
            url = ""

    def mj_sv(self):
        try:
            data = self.sock.recv(1024)
            if data:
                print("Ver: ",data.decode())
        except:
            print("Algo Fallo")
            self.sock.close()
            sys.exit()

    def mandarmensj(self, url):
        self.sock.send(url.encode())

client = Cliente()