import socket

# Variables del servidor TCP
TCP_PORT = 0
BUFFER_SIZE = 1024

# Variables del juego global
juego_categoria = ""
longitud_palabra = 0
progreso_palabra = list("")
letras_adivinadas = []
intentos = 0
opciones = False
ganar_juego = False


# Dibuja el progreso actual de la palabra adivinar.
def draw_progress():
    global opciones
    global progreso_palabra

    if not opciones:
        counter = 0
        while counter < longitud_palabra:
            # Agrega un guión bajo a la cadena de progreso de la palabra
            progreso_palabra += "_"

            counter += 1

        opciones = True

    # Devuelve el progreso de la palabra como una cadena con espacios entre cada carácter.
    return " ".join(progreso_palabra)


# Dibuja un personaje ASCII hangman,
# palabra progreso y letras adivinadas.
# Toma el número de intento como argumento
def draw_hangman(attempt):
    if attempt == 0:
        print(" _________     ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 1:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 2:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 4:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\\  ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 5:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\\  ")
        print("|        /     ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)
    elif attempt == 6:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\\  ")
        print("|        / \\  ")
        print("|              ")
        print("|              ")
        print("palabra:", draw_progress())
        print("letras adivinadas:", letras_adivinadas)


# Crea el socket TCP para un juego potencial de MP
host_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# OpCodes
# 0. Salir del juego sin advertencia.
# 1. juego de configuración
# 2. Carta letra
# 3. Jugador gana
# 4. Jugador pierde


# Enviar código de operación como el mensaje inicial y datos adicionales como mensajes adicionales
def send_opcode(opcode):
    # Intenta capturar para enviar correctamente el código de operación al servidor
    try:

        # Envía el opcode
        host_connection.send(str.encode(opcode))

        # Continúa en bucle hasta que se recibe un eco de opcode
        while True:
            # Espera un opcode echo
            opcode_recv = host_connection.recv(BUFFER_SIZE)

            if bytes.decode(opcode_recv) == "0":

                # Cierra la conexión del servidor
                host_connection.close()
                break

            # Manejo del código de configuración del juego.
            elif bytes.decode(opcode_recv) == "1":

                # Le dice al usuario en qué datos se está esperando
                print("Esperando que el anfitrión elija una palabra y categoría ...")

                # Continúa en bucle hasta que se reciben datos adicionales
                while True:
                    # Espera datos adicionales
                    data_recv = host_connection.recv(BUFFER_SIZE)

                    # Ram una vez que se han recibido los datos
                    if data_recv:
                        # Divide los datos adicionales en las comas.
                        data_recv = bytes.decode(data_recv).split(",")

                        # Almacena la categoría de palabra elegida en una variable global
                        global juego_categoria
                        juego_categoria = data_recv[0]

                        # Almacena la longitud de palabra elegida en una variable global
                        global longitud_palabra
                        longitud_palabra = int(data_recv[1])

                        #Le dice al usuario cuál es la categoría de palabra
                        print("La categoría de la palabra es:", juego_categoria)

                        #Sale del bucle de escucha
                        break
            # Letra adivinar manejo de código de operación
            elif bytes.decode(opcode_recv) == "2":

                # Hace referencia a la lista global de letras adivinadas
                global letras_adivinadas

                # Pide al usuario una letra adivina
                chosen_letter = str(input("adiniva una letra: ")).lower()

                # Bucea hasta que el usuario adivine una letra válida.
                while chosen_letter == "" \
                        or chosen_letter in letras_adivinadas \
                        or not chosen_letter.isalpha()\
                        or len(chosen_letter) > 1:
                    # Le dice al usuario que su suposición no es válida
                    print("Esa no es una letra válida, por favor intente de nuevo!")

                    # Pide al usuario que adivine una letra.
                    chosen_letter = str(input("adiniva una letra: "))

                letras_adivinadas += chosen_letter

                # Crea un flujo de datos vacío
                game_data = ""

                # Agrega la letra adivinada al flujo de datos
                game_data += chosen_letter

                # Envía el flujo de datos al servidor
                host_connection.send(str.encode(game_data))

                # Separador para propósitos de formato.
                print("----------------------------")

                # Continúa en bucle hasta que se reciben datos adicionales
                while True:
                    # Espera datos adicionales
                    data_recv = host_connection.recv(BUFFER_SIZE)
                    # Ram una vez que se han recibido los datos
                    if data_recv:
                        # Comprueba si la letra adivina fue correcta
                        if bytes.decode(data_recv) != "false":
                            # Le dice al usuario que su conjetura fue correcta
                            print("Tu suposición fue correcta!")

                            # Divide los datos adicionales en las comas.
                            data_recv = bytes.decode(data_recv).split(",")

                            # Agrega la letra elegida a los espacios correctos.
                            # en la palabra progreso
                            for x in range(0, len(data_recv) - 1):
                                progreso_palabra[int(data_recv[x])]\
                                    = chosen_letter

                            # Comprueba si la palabra progreso contiene
                            # más guiones bajos
                            if "_" not in progreso_palabra:
                                # Envía al jugador el código de operación
                                send_opcode("3")
                        else:
                            global intentos

                            # Agrega uno a la variable de intentos globales
                            intentos += 1

                            # Comprueba si el usuario está fuera de intentos todavía
                            if intentos != 6:

                                # Le dice al usuario que su letra era incorrecta
                                if intentos != 5:
                                    print("Tu letra fue incorrecta, tienes",
                                          6 - intentos, "¡intentos restantes!")
                                else:
                                    print("Tu letra fue incorrecta, tienes",
                                          6 - intentos, "¡intentos restantes!")
                            else:
                                # Envía al jugador a perder el opcode
                                send_opcode("4")
                            # Sale del bucle de escucha
                        break
            elif opcode == "3":
                # Establece la variable win en true
                global ganar_juego
                ganar_juego = True

                while True:
                    # Espera datos adicionales
                    data_recv = host_connection.recv(BUFFER_SIZE)
                    # Ram una vez que se han recibido los datos
                    if data_recv:
                        break
            elif opcode == "4":
                while True:
                    # Espera datos adicionales
                    data_recv = host_connection.recv(BUFFER_SIZE)
                    # Ram una vez que se han recibido los datos
                    if data_recv:
                        break
            # Ran una vez que se han recibido los datos
            if opcode_recv:
                # Sale del bucle de escucha
                break

    # Excepción de captura para cualquier excepción de socket
    except ConnectionError:
        # Mata el programa si no se puede alcanzar el servidor
        print("¡Error al conectarse al servidor!")
        quit()


# Mensajes de bienvenida
print("¡Bienvenido al juego del ahorcado!")
print("El objetivo del juego es adivinar qué palabra es "
      "El oponente elige para usted letra por letra")

# Pide al usuario una IP y verifica si es válida
TCP_IP = input("Ingrese la IP del host (127.0.0.1 para localhost): ")
try:
    socket.inet_aton(TCP_IP)
except socket.error:
    print("¡Esa no es una IP válida!")
    print("¡Programa de salida!")
    quit()

# Pide al usuario un puerto y comprueba si es válido
while TCP_PORT < 1024 or TCP_PORT > 65535:
    try:
        TCP_PORT = int(input("Ingrese el puerto del host: "))
    except ValueError:
        pass

while host_connection:
    # Intenta capturar para manejar las excepciones de conexión de socket
    try:
        # Se conecta al host del juego
        host_connection.connect((TCP_IP, TCP_PORT))
    except ConnectionError:
        # Mata el programa si no puede conectarse al servidor
        print("¡No se puede conectar al servidor!")
        quit()
    break

# Envía el opcode de configuración del juego
send_opcode("1")


# Dibuja el verdugo vacío
draw_hangman(0)


# Comprueba si el usuario tiene algún intento todavía y si ha ganado el juego
while intentos < 6 and not ganar_juego:
    # Envía la letra adivina
    send_opcode("2")
    # Dibuja el  ASCII así como el progreso de la palabra.
    # y letras adivinadas
    draw_hangman(intentos)

# Maneja el juego gana y pierde y envía el código de operación "0"
# cierra la conexión después
if ganar_juego:
    print("Adivinaste la palabra correctamente, ganas!!")
    print("GRACIAS POR JUGAR!")
else:
    print("Te quedaste sin letras, ¡pierdes!")
    print("GRACIAS POR JUGAR!")
send_opcode("0")