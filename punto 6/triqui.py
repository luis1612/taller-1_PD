from tkinter import *
import random
from tkinter import messagebox

# ---------------------------------------------------

# VARIABLE UTILIZADA PARA DEFINIR EL TURNO
turn = None
salir = False

# ---------------------------------------------------

# FUNCIÓN PARA DEFINIR EL TURNO Y MOSTRARLO
def turno():
	global turn
	global salir
	if salir:
		root.quit()
	else:
		if turn == None:
			turn = random.randrange(1,3)
		elif turn == 1:
			turn = 2
		elif turn == 2:
			turn = 1


# ---------------------------------------------------

# FUNCIÓN SI APRETAMOS UN BOTÓN YA SELECCIONADO

def error():
	messagebox.showerror("Error", "La casilla que seleccionaste ya estaba ocupada, reintentalo")
	messagebox.showinfo("Turno", "Es el turno del jugador número: {}".format(turn))


# ---------------------------------------------------


# FUNCIÓN PARA MOSTRAR LOS CAMBIOS EN LA PANTALLA
def verificarturno():
	global turn
	text = ""
	if turn == 1:
		text = "X"
	elif turn == 2:
		text = "O"

	return text

# ---------------------------------------------------



# FUNCIÓN PARA CADA BOTÓN
def verificaruno():
	if uno.get() == "":
		uno.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificardos():
	if dos.get() == "":
		dos.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificartres():
	if tres.get() == "":
		tres.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarcuatro():
	if cuatro.get() == "":
		cuatro.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarcinco():
	if cinco.get() == "":
		cinco.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarseis():
	if seis.get() == "":
		seis.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarsiete():
	if siete.get() == "":
		siete.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarocho():
	if ocho.get() == "":
		ocho.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

def verificarnueve():
	if nueve.get() == "":
		nueve.set(verificarturno())
		comprobar()
		turno()
	else:
		error()

# ---------------------------------------------------


# COMPROBACION DE QUE SE HAYA HECHO TRIQUI

def comprobar():

	global turn


	one = uno.get()
	two = dos.get()
	three = tres.get()
	four = cuatro.get()
	five = cinco.get()
	six = seis.get()
	seven = siete.get()
	eight = ocho.get()
	nine = nueve.get()



	if one != "" and one == two and two == three:
		tateti()
	elif four != "" and four == five and five == six:
		tateti()
	elif seven != "" and seven == eight and eight == nine:
		tateti()
	elif one != "" and one == four and four == seven:
		tateti()
	elif two != "" and two == five and five == eight:
		tateti()
	elif three != "" and three == six and six == nine:
		tateti()
	elif one != "" and one == five and five == nine:
		tateti()
	elif three != "" and three == five and five == seven:
		tateti()
	elif one != "" and two != "" and three != "" and four != "" and five != "" and six != "" and seven != "" and eight != "" and nine != "":
		reiniciar()




# -----------------------------------------------


# FUNCIÓN EN CASO DE TRIQUI

def tateti():
	global turn
	global salir
	messagebox.showwarning("Ganaste!!!", "El ganador de la partida es el jugador número: {}".format(turn))
	resp = messagebox.askokcancel("¿Revancha?","¿Quieres volver a jugar?")
	if resp:
		reiniciar()
	else:
		salir = True


# -----------------------------------------------

# FUNCIÓN PARA REINICIAR EL JUEGO

def reiniciar():
	global turn
	uno.set("")
	dos.set("")
	tres.set("")
	cuatro.set("")
	cinco.set("")
	seis.set("")
	siete.set("")
	ocho.set("")
	nueve.set("")
	turn = None


# -----------------------------------------------


# INICIO DE LA VENTANA
root = Tk()
root.title("Triqui")
root.resizable(0,0)


# -----------------------------------------------


# VARIABLES PARA CADA BOTÓN
uno = StringVar()
dos = StringVar()
tres = StringVar()
cuatro = StringVar()
cinco = StringVar()
seis = StringVar()
siete = StringVar()
ocho = StringVar()
nueve = StringVar()


# -----------------------------------------------

# CONFIGURACION DE LOS BOTONES
pos1 = Button(root, textvariable=uno, command=verificaruno)
pos1.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos1.grid(row=0, column=0, padx=5, pady=5)

pos2 = Button(root, textvariable=dos, command=verificardos)
pos2.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos2.grid(row=0, column=1, padx=5, pady=5)

pos3 = Button(root, textvariable=tres, command=verificartres)
pos3.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos3.grid(row=0, column=2, padx=5, pady=5)

pos4 = Button(root, textvariable=cuatro, command=verificarcuatro)
pos4.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos4.grid(row=1, column=0, padx=5, pady=5)

pos5 = Button(root, textvariable=cinco, command=verificarcinco)
pos5.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos5.grid(row=1, column=1, padx=5, pady=5)

pos6 = Button(root, textvariable=seis, command=verificarseis)
pos6.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos6.grid(row=1, column=2, padx=5, pady=5)

pos7 = Button(root, textvariable=siete, command=verificarsiete)
pos7.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos7.grid(row=2, column=0, padx=5, pady=5)

pos8 = Button(root, textvariable=ocho, command=verificarocho)
pos8.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos8.grid(row=2, column=1, padx=5, pady=5)

pos9 = Button(root, textvariable=nueve, command=verificarnueve)
pos9.config(font=("Ventana", 15), justify="center", width=10, height=5)
pos9.grid(row=2, column=2, padx=5, pady=5)

# -----------------------------------------------

turno()

# -----------------------------------------------
# FIN DEL PROGRAMA
root.mainloop()
