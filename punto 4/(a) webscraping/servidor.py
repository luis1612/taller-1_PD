import requests
import bs4
import lxml
import socket
import sys

class Servidor():
    def __init__(self, host="localhost", port=8999):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(1)

        print(" La Conexion fue Exitosa.")
        conect, direccion = self.sock.accept()

        mj = conect.recv(1024)

        while True:
            if mj.decode() == 'a':
                respuesta = self.web('https://www.booking.com/?aid=1546873')
                conect.send(respuesta.encode())
            else:
                print("Salir")
                self.sock.close()
                sys.exit()

    def web(self, url):
        try:
            array = []
            resultado = requests.get(url)
            soup = bs4.BeautifulSoup(resultado.text, 'lxml')
            for i in soup.select('h3'):
                array.append(i.text)
        except:
            print("Algo Fallo")
            self.sock.close()

        return str(array)

server = Servidor()