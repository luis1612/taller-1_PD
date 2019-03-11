import socket

# Variables del servidor TCP
TCP_IP = '127.0.0.1'
TCP_PORT = 0
BUFFER_SIZE = 1024

# variables globales del juego
GAME_WORD = ""
GAME_CATEGORY = ""
GAME_OPPONENT_ATTEMPTS = 0

# OpCodes
# 0. Salir del juego sin advertencia.
# 1. juego de configuración
# 2. Carta conjetura
# 3. Jugador gana
# 4. Jugador pierde


def handle_opcode(opcode):
    # Repetir el código de operación al cliente.
    client_connection.send(opcode)

    # Cerrar el código de operación del programa
    if bytes.decode(opcode) == "0":
        client_connection.close()
        quit()

    # Código de configuración del juego
    elif bytes.decode(opcode) == "1":
        global GAME_CATEGORY
        global GAME_WORD
        # Crea un flujo de datos vacío
        game_data = ""

        # Establece la categoría de palabra y la agrega al flujo de datos
        GAME_CATEGORY = input("Elige una categoría: ")
        while not GAME_CATEGORY.isalpha() or len(GAME_CATEGORY) < 1:
            print("Esa no es una categoría válida, por favor intente de nuevo!")
            GAME_CATEGORY = input("Elige una categoría:")
        game_data += GAME_CATEGORY

        game_data += ","

        # Establece la palabra y la almacena en una variable global

        GAME_WORD = input("Elige una palabra: ").lower()
        while not GAME_WORD.isalpha() or len(GAME_WORD) < 1:
            print("Esa no es una opción de palabra válida, por favor intente de nuevo!")
            GAME_WORD = input("Elige una palabra: ").lower()

        # Agrega la longitud de las palabras elegidas al flujo de datos
        game_data += str(len(GAME_WORD))

        # Envía el flujo de datos al cliente
        client_connection.send(str.encode(game_data))

    # Letra adivina recibido código de operación
    elif bytes.decode(opcode) == "2":
        global GAME_OPPONENT_ATTEMPTS

        print("Esperando a que tu oponente adivine una letra ...")

        while True:
            # Espera datos adicionales
            data_recv = client_connection.recv(BUFFER_SIZE)

            # Ram una vez que se han recibido los datos
            if data_recv:

                # Decodifica la letra recibida
                received_letter = bytes.decode(data_recv)

                # Le dice al anfitrión qué letra fue adivinada
                print("Tu oponente adivinó la letra:", received_letter)

                # Le dice al usuario que su letra era incorrecta
                if GAME_OPPONENT_ATTEMPTS != 5:
                    print("Tu oponente tiene",
                          5 - GAME_OPPONENT_ATTEMPTS, "¡intentos restantes!")
                else:
                    print("Tu oponente tiene",
                          5 - GAME_OPPONENT_ATTEMPTS, "¡intentos restantes!")

                # Separador para propósitos de formato.
                print("----------------------------")

                # Comprueba si la letra adivinada está en la palabra elegida
                if received_letter in GAME_WORD:

                    # Crea una lista de todos los índices de la palabra elegida.
                    # que contienen la letra adivinada
                    success_indexes = [
                                       i for i,
                                       letter in enumerate(GAME_WORD)
                                       if letter == received_letter
                                      ]

                    # Crea un flujo de datos vacío
                    game_data = ""

                    # Recorre cada elemento .
                    # lista de índices
                    for x in range(0, len(success_indexes)):
                        # Agrega cada índice de letras a la secuencia de datos usando
                        # comas como separadores
                        game_data += str(success_indexes[x])
                        game_data += ","

                    # Envía la letra de datos al cliente.
                    client_connection.send(str.encode(game_data))

                # Devuelve falso si la letra adivinada no es
                # en la palabra elegida
                else:
                    # Agrega uno al contador de intentos del oponente.
                    GAME_OPPONENT_ATTEMPTS += 1

                    # Envía un código falso al cliente
                    client_connection.send(str.encode("false"))

                # Sale del bucle de escucha
                break
    # Jugador gana manejo de opcode
    elif bytes.decode(opcode) == "3":

        # Le dice al anfitrión que el oponente ganó
        print("Tu oponente ha ganado!")
        print("¡Gracias por jugar!")

        # Envía una respuesta exitosa al cliente
        client_connection.send(str.encode("true"))
    # Jugador pierde el manejo del código de operación
    elif bytes.decode(opcode) == "4":
        # Le dice al anfitrión que el oponente perdió
        print("Tu oponente se ha quedado sin adivinanzas, tú ganas!")
        print("¡Gracias por jugar!")

        # Envía una respuesta exitosa al cliente
        client_connection.send(str.encode("true"))



# Mensajes de bienvenida
print("Bienvenido al juego del ahorcado!")
print("El objetivo del juego es elegir una palabra de una categoría que "
      "elige y espera que tu oponente no pueda adivinarlo en sus 6 intentos")


# Pide al host un puerto y comprueba si es válido
while TCP_PORT < 1024 or TCP_PORT > 65535:
    try:
        TCP_PORT = int(input("Elija un puerto entre 1024 y 65535: "))
    except ValueError:
        pass

# Abre el socket del servidor y se enlaza al puerto dado
game_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
game_socket.bind((TCP_IP, TCP_PORT))
game_socket.listen(1)

print("Esperando la conexión del cliente ...")

# game_socket.accept () devuelve dos valores, la conexión y la información adicional.
# client_connection se establece en la conexión de socket y la dirección_de_cliente
# se establece en la información de complemento de socket
client_connection, client_address = game_socket.accept()


# Imprime la conexión IP del cliente.
print('Cliente IP:', client_address[0])

# Escucha datos mientras exista una conexión de cliente
while client_connection:
    # Almacena los datos recibidos en la variable de datos.
    data = client_connection.recv(BUFFER_SIZE)

    # Maneja el código de operación recibido
    handle_opcode(data)

# Cierra la conexión al final del programa.
client_connection.close()
