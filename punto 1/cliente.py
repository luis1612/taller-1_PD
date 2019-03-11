import socket
import sys

mi_socket = socket.socket()
mi_socket.connect(('127.0.0.1', 9090))

try:

    usuario = input(" ingrese el usuario => ")
    nuevo = input('Ingrese un nuevo nombre de usuario>>')
    mensaje = usuario + ',' + nuevo
    print('Enviando %s' % mensaje, file=sys.stderr)
    mi_socket.send(mensaje.encode())

    # buscando respuesta
    caracteres_recibidos = 0
    caracteres_esperador = len(mensaje.encode())

    # buscando respuesta
    caracteres_recibidos = 0
    caracteres_esperador = len(mensaje.encode())

    while caracteres_recibidos < caracteres_esperador:
        datos = mi_socket.recv(64).decode()
        caracteres_recibidos += len(datos)
        print('recibiendo %s' % str(datos))

finally:
    print('Cerrando socket', file=sys.stderr)
    mi_socket.close()
