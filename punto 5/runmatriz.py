# -*- coding: utf-8 -*-
import matriz
from pip._vendor.distlib.compat import raw_input


def main():
    op = " "

    while op != "s" and op != "S":
        print("------------------------------------------")
        print("\t\tMENU\t\t")
        print("(a). Determinante ")
        print("(b). Traspuesta ")
        print("(c). Inversa ")
        print("(d). Multiplicar matriz por un numero")
        print("(e). Matriz elevada a una Potencia ")
        print("(f). Matriz Simetrica ")
        print("(g). Matriz Identidad ")
        print("************************")
        print ("Operaciones con dos matrices:")
        print("(h). A * B")
        print("(i). A - B")
        print("(j). A + B")
        print("(s).Salir")
        op=input("Ingrese una opción válida: ")

        if op == "a" or op == "A":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            vali=matrizA.cuadrada()
            if vali:
                print ("1. Matriz manual")
                print ("2. Matriz Automatica")
                sel=input("Seleccione Tipo")
                if sel=="1":
                    matrizA.Llenar_manual()
                else:
                    matrizA.Llenar_m()
                print ("Matriz Generada:")
                matrizA.Print_m()
                print ("Determinante de la matriz:")
                print (matrizA.getMatrixDeternminant(matrizA.datam()))
            else:
                print ("La matriz debe ser Cuadrada ej: 2x2,3x3....nxn")
        elif op == "b" or op == "B":
            matrizA = matriz.Matriz()
            print ("Matriz A")
            matrizA.Crear_m()
            matrizA.Llenar_m()
            print ("Matriz Generada")
            matrizA.Print_m()
            matrizC = matriz.Matriz(matrizA.columnas, matrizA.filas)
            matrizC.Crear_m()
            matrizC.traspuesta(matrizA.datam())
            print ("Matriz Traspuesta")
            matrizC.Print_m()
        elif op == "c" or op == "C":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            print ("Matriz Generada")
            matrizA.Print_m()
            print ("Matriz Inversa")
            print (matrizA.getMatrixInverse(matrizA.datam()))
        elif op == "d" or op == "D":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            print ("matriz Generada")
            matrizA.Print_m()
            num = int(raw_input('Ingrese número por el que se multiplicara la matriz: \n'))
            matrizA.multireal(num)
            print ("Matriz Resultado")
            matrizA.Print_m()
        elif op == "E" or op == "e":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            print ("Matriz Generada")
            matrizA.Print_m()
            pot=int(raw_input("Ingrese Potencia"))
            print (matrizA.getPow(pot))
        elif op == "f" or op == "F":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_manual()
            vali = matrizA.cuadrada()
            if vali:
                print ("Matriz Generada")
                matrizA.Print_m()
                matrizA.simetrica()
            else:
                print ("Error Matriz debe ser Cuadrada")
        elif op == "g" or op == "G":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            vali = matrizA.cuadrada()
            if vali:
                matrizA.identidad()
                print ("Matriz Identidad")
                matrizA.Print_m()
            else:
                print ("Error Matriz debe ser Cuadrada")
        elif op == "h" or op == "H":
            matrizA = matriz.Matriz()
            print ("Matriz A")
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()
            matrizB = matriz.Matriz()
            print ("Matriz B")
            matrizB.Crear_m()
            matrizB.Llenar_m()
            matrizB.Print_m()
            valida=matrizB.valida_m(matrizA.columnas,matrizB.filas)
            if valida:
                print ("Error las Columnas de la Matriz A debe ser igual a las filas de la Matriz B ")
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.multi_m(matrizA.datam(),matrizB.datam(),matrizB.filas)
                print ("Matriz Resultado")
                matrizC.Print_m()
        elif op == "i" or op == "I":
            matrizA = matriz.Matriz()
            matrizA.Crear_m()
            matrizA.Llenar_m()
            print ("Matriz A")
            matrizA.Print_m()

            matrizB = matriz.Matriz()
            matrizB.Crear_m()
            matrizB.Llenar_m()
            print ("Matriz B")
            matrizB.Print_m()
            vali=matrizB.valida_sumres(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            if vali:
                print("Error no es posible la operación, las matrices deben tener el mismo tamaño")
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.sum_m(matrizA.datam(), matrizB.datam())
                print("Matriz Resultado")
                matrizC.Print_m()
        elif op == "j" or op == "J":
            matrizA = matriz.Matriz()
            print("Matriz A")
            matrizA.Crear_m()
            matrizA.Llenar_m()
            matrizA.Print_m()

            matrizB = matriz.Matriz()
            print("Matriz B")
            matrizB.Crear_m()
            matrizB.Llenar_m()
            matrizB.Print_m()

            vali=matrizB.valida_sumres(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            if vali:
                print("Error no es posible la operación, las matrices deben tener el mismo tamaño")
            else:
                matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
                matrizC.Crear_m()
                matrizC.rest_m(matrizA.datam(), matrizB.datam())
                print ("Matriz Resultado")
                matrizC.Print_m()
        elif op == "S" or op == "s":
            print ("Gracias por utilizar nuestro servicio de calculadora de matrices")
            exit()
        else:
            print("Digite una opcion valida \n")

if __name__ == '__main__':
    main()