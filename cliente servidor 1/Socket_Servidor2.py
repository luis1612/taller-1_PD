# Socket servidor

import socket
import sys

#Creando el socket TCP/IP
socket_enlace = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Enlace de socket y puerto
direccion_servidor = ('localhost', 9999)
print('Empezando a escuchar en %s en el puerto %s' %direccion_servidor, file = sys.stderr)
socket_enlace.bind(direccion_servidor)

#Escuchando conexiones entrantes
socket_enlace.listen()

while True:
        #Esperando conexion
        print('Esperand para conectarse', file=sys.stderr)
        conexion, direccion_cliente = socket_enlace.accept()

        try:
                
                print('Esperando para conectarse', file=sys.stderr)

                # Recibe los datos en trozos y reetransmite
                while  True:
                        datos = conexion.recv(64).decode()
                        print('recibo %s' %datos, file =
                              sys.stderr)   
                        if datos:
                                print('Enviando mensaje de regreso al cliente', file=sys.stderr)
                                conexion.send(datos.encode())
                                puertonuevo,ipnueva = datos.split(',');
                                print(ipnueva)
                                print(puertonuevo)
                        else:
                                print('Ya no hay mas datos', direccion_cliente, file=sys.stderr)
                                break
        finally:
                #cerrando conexion
                conexion.close()
                
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Nuevos variables
puertonuevo = str(puertonuevo)
ipnueva = int(ipnueva)
#print(ipnueva)
#print(puertonuevo)

#Enlace de socket y puerto
direccion_servidor = (ipnueva, puertonuevo)
print('Empezando a escuchar en %s en el puerto %s' %direccion_servidor, file = sys.stderr)
socket_enlace.bind(direccion_servidor)

#Escuchando conexiones entrantes
socket_enlace.listen()

while True:
        #Esperando conexion
        print('Esperand para conectarse', file=sys.stderr)
        conexion, direccion_cliente = socket_enlace.accept()

        try:
                
                print('Esperando para conectarse', file=sys.stderr)

                # Recibe los datos en trozos y reetransmite
                while  True:
                        datos = conexion.recv(64).decode()
                        print('recibo %s' %datos, file = sys.stderr)   
                        if datos:
                                print('Enviando mensaje de regreso al cliente', file=sys.stderr)
                                conexion.send(datos.encode())
                                #mensageenviado,puertonuevo,ipnueva = datos.split(',');
                                #print(ipnueva)
                        else:
                                print('Ya no hay mas datos', direccion_cliente, file=sys.stderr)
                                break
        finally:
                #cerrando conexion
                conexion.close()



#Comandos DOS para manejo de PID
#netstat -a -o   se ve todas las conexiones remotas y locales
# taskkill /PID 5000 /F 
