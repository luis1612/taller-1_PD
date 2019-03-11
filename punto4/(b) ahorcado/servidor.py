import socket

# TCP server variables
TCP_IP = '127.0.0.1'
TCP_PORT = 0
BUFFER_SIZE = 1024

# Global game variables
palabra = ""
juego_categoria = ""
intentos_de_juego_oponentes = 0

# OpCodes
# 0. Salir del juego sin advertencia.
# 1. juego de configuración
# 2. Carta conjetura
# 3. Jugador gana
# 4. Jugador pierde


def handle_opcode(opcode):
    # Echo the opcode back to the client
    client_connection.send(opcode)

    # Close program opcode
    if bytes.decode(opcode) == "0":
        client_connection.close()
        quit()
    # Game setup opcode
    elif bytes.decode(opcode) == "1":
        global juego_categoria
        global palabra
        # Creates an empty data stream
        datos_juego = ""

        # Sets the word category and adds it to the data stream
        juego_categoria = input("Elige una categoría: ")
        while not juego_categoria.isalpha() or len(juego_categoria) < 1:
            print("Esa no es una categoría válida, por favor intente de nuevo!")
            juego_categoria = input("Elige una categoría: ")
        datos_juego += juego_categoria

        datos_juego += ","

        # Sets the word and stores it in a global variable

        palabra = input("Elige una palabra:").lower()
        while not palabra.isalpha() or len(palabra) < 1:
            print("Esa no es una opción de palabra válida, por favor intente de nuevo!")
            palabra = input("Elige una palabra: ").lower()

        # Adds the chosen words length to the data stream
        datos_juego += str(len(palabra))

        # Sends the data stream to the client
        client_connection.send(str.encode(datos_juego))
    # Letter guess received opcode
    elif bytes.decode(opcode) == "2":
        global intentos_de_juego_oponentes

        print("Esperando a que tu oponente adivine una letra ...")

        while True:
            # Waits for additional data
            data_recv = client_connection.recv(BUFFER_SIZE)

            # Ran once data has been received
            if data_recv:
                # Decodes the received letter guess
                received_letter = bytes.decode(data_recv)

                # Tells the host what letter was guessed
                print("Tu oponente adivinó la letra:", received_letter)

                # Tells the user their guess was incorrect
                if intentos_de_juego_oponentes != 5:
                    print("Tu oponente tiene",
                          5 - intentos_de_juego_oponentes, "¡intentos restantes!")
                else:
                    print("Your opponent has",
                          5 - intentos_de_juego_oponentes, "¡intentos restantes!")

                # Separator for formatting purposes
                print("----------------------------")

                # Checks if the guessed letter is in the chosen word
                if received_letter in palabra:
                    # Creates a list of all the indexes of the chosen word
                    # that contain the guessed letter
                    success_indexes = [
                                       i for i,
                                       letter in enumerate(palabra)
                                       if letter == received_letter
                                      ]

                    # Creates an empty data stream
                    datos_juego = ""

                    # Loops through each element in the successful
                    # indexes list
                    for x in range(0, len(success_indexes)):
                        # Adds each letter index to the data stream using
                        # commas as separators
                        datos_juego += str(success_indexes[x])
                        datos_juego += ","
                    # Sends the letter guess data to the client
                    client_connection.send(str.encode(datos_juego))
                # Returns false if the guessed letter is not
                # in the chosen word
                else:
                    # Adds one to the opponent attempt counter
                    intentos_de_juego_oponentes += 1

                    # Sends a false code to the client
                    client_connection.send(str.encode("false"))

                # Breaks out of the listening loop
                break
    # Player win opcode handling
    elif bytes.decode(opcode) == "3":
        # Tells the host that the opponent won
        print("Tu oponente ha ganado!")
        print("¡Gracias por jugar!")

        # Sends a success response to client
        client_connection.send(str.encode("true"))
    # Player lose opcode handling
    elif bytes.decode(opcode) == "4":
        # Tells the host that the opponent lost
        print("Tu oponente se ha quedado sin adivinanzas, tú ganas!")
        print("¡Gracias por jugar!")

        # Sends a success response to client
        client_connection.send(str.encode("true"))


# Welcome messages
print("Bienvenido al juego del ahorcado!")
print("El objetivo del juego es elegir una palabra de una categoría que "
      "elige y espera que tu oponente no pueda adivinarlo en sus 6 intentos")

# Asks the host for a port and checks if it is valid
while TCP_PORT < 1024 or TCP_PORT > 65535:
    try:
        TCP_PORT = int(input("Elija un puerto entre 1024 y 65535: "))
    except ValueError:
        pass

# Opens the server socket and binds to the given port
game_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
game_socket.bind((TCP_IP, TCP_PORT))
game_socket.listen(1)

print("Esperando la conexión del cliente ...")

# game_socket.accept() returns two values, the connection and the addr info
# client_connection is set to the socket connection and client_address
# is set to the socket addr info
client_connection, client_address = game_socket.accept()

# Prints the client's connection IP
print('Client IP:', client_address[0])

# Listens for data as long as a client connection exists
while client_connection:
    # Stores received data in data variable
    data = client_connection.recv(BUFFER_SIZE)
    # Handles the received opcode
    handle_opcode(data)
# Closes the connection at the end of the program
client_connection.close()
