#Socket cliente

import socket
import sys
import time


# Crea el socket TCP/IP
socket_enlace = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cuando el servidor esta en escucha, conecta el socket en el puerto establecido
direccion_servidor = ('localhost', 9999)

print('Conectandose a %s por el puerto %s' %direccion_servidor, file=sys.stderr)
socket_enlace.connect(direccion_servidor)

try:
        
        #enviando datos
       
        #mensaje= input('Ingrese el nuevo mensage>>')
        usuario= input('Ingrese el usuario>>')
        password= input('Ingrese la password>>')
        mensaje=usuario+','+password
        print('Enviando %s' %mensaje, file=sys.stderr)
        socket_enlace.send(mensaje.encode())
       
        
         #buscando respuesta
        caracteres_recibidos = 0
        caracteres_esperador = len(mensaje.encode())

        while caracteres_recibidos < caracteres_esperador:
                  datos = socket_enlace.recv(64).decode()
                  caracteres_recibidos += len(datos)
                  print('recibiendo %s' %str(datos))

finally:
        print('Cerrando socket', file= sys.stderr)
        socket_enlace.close()
        
#variables
host = str(host)
puerto = int(puerto)
#print(puerto)
#print(host)
time.sleep(2)
# Crea el socket TCP/IP
socket_enlace = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Enviar nuevo mensaje al Servidor
print(host)
print(puerto)
direccion_servidor = (host,puerto)
print('Conectandose a %s por el puerto %s' % direccion_servidor, file=sys.stderr)
socket_enlace.connect(direccion_servidor)

try:
    # Enviando datos
    mensaje = input('Introduce el mensaje que se transmite mediante el socket: ')
    print('Conectandose a: %s' % mensaje, file=sys.stderr)
    socket_enlace.sendall(mensaje.encode())

    # Buscando respuesta
    caracteres_recibidos = 0
    caracteres_esperados = len(mensaje.encode())

    while caracteres_recibidos < caracteres_esperados:
        datos = socket_enlace.recv(128).decode()
        caracteres_recibidos += len(datos)
        print('recibidos %s' % str(datos))

finally:
    print('Cerrando socket', file=sys.stderr)
    socket_enlace.close()

