# -*- coding: utf-8 -*-
import random

class Matriz(object):
    def __init__(self, filas=None, columnas=None):

        if filas:
            self.filas =filas
        else:
            try:
                self.filas = int (input(" Ingrese número de filas"))
            except ValueError:
                print("ATENCIÓN: Debe ingresar un número entero.")
                exit()

        if columnas:
            self.columnas = columnas
        else:
            try:
                self.columnas = int(input(" Ingrese número de columnas"))
            except ValueError:
                print("ATENCIÓN: Debe ingresar un número entero.")
                exit()



    def Crear_m(self):
      self.matriz=[]
      for f in range(self.filas):
          self.matriz.append([0]*self.columnas)

    def Llenar_m(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(-10, 10)

    def Llenar_manual(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = input("Ingrese %d,%d: " % (f, c))

    def Print_m(self):
        print (self.matriz)

    def datam(self):
        return self.matriz

    def valida_m(self,colA,filB):
        if colA != filB:
            return True
        else:
            return False

    def multi_m(self,matrizA,matrizB,filaB):
        for f in range(self.filas):
            for c in range(self.columnas):
                for k in range(filaB):
                    self.matriz[f][c]+=matrizA[f][k]*matrizB[k][c]

    def multireal(self,nreal):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = self.matriz[f][c] * nreal

    def valida_sumres(self,filA, colA, filB,colB):
        if (colA != colB) or (filA != filB):
            return True
        else:
            return False

    def sum_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] + matrizB[f][c]

    def rest_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] - matrizB[f][c]

    def copy(self,m):
        self.result = []
        for f in m:
            self.result.append(f[:])
        return self.result

    def combinacion(self,m, i, j, e):
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def intercambiaFilas(self,m, i, j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self,m, f, e):
        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def primeroNoNulo(self,m, i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def determinante(self,matr):
        m = self.copy(matr)
        n = len(m)
        det = 1
        for i in range(n):
            j = self.primeroNoNulo(m, i)
            if j == n:
                return 0
            if i != j:
                det = -1 * det
                self.intercambiaFilas(m, i, j)
            det = det * m[i][i]
            self.multiplicaFila(m, i, 1. / m[i][i])
            for k in range(i + 1, n):
                self.combinacion(m, i, k, -m[k][i])
        print (int(det))

    def cuadrada(self):
        if self.filas == self.columnas:
            return True
        else:
            return False

    def traspuesta(self,mA):
       # if self.cuadrada():
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = mA[c][f]

    def simetrica(self):
        band = True
        for f in range(self.filas):
            for c in range(self.columnas):
                if (self.matriz[f][c] != self.matriz[c][f]):
                    band = False
                    break
        if (band):
            print("Matriz Simetrica")
        else:
            print("Matriz no es Simetrica")

    def identidad(self):
        for f in range(self.filas):
            self.matriz[f][f] = 1

    def multiply(self,matriz1, matriz2,fila):
        res = []
        for f in range(fila):
            res.append([0] * fila)

        for i, row in enumerate(res):
            for j in range(0, len(row)):
                for k in range(0, len(row)):
                    res[i][j] += matriz1[i][k] * matriz2[k][j]
        return res

    def getPow(self, pow):
        powerhash = {}
        if pow in powerhash.keys():
           return powerhash[pow]
        if pow == 1:
            return self.matriz
        if pow == 2:
            powerhash[pow] = self.multiply(self.matriz, self.matriz,self.filas)
            return powerhash[pow]
        if pow % 2 == 0:
            powerhash[pow] = self.multiply(self.getPow(pow / 2), self.getPow(pow / 2),self.filas)
        else:
            powerhash[pow / 2 + 1] = self.multiply(self.getPow(pow / 2), self.matriz,self.filas)
            powerhash[pow] = self.multiply(self.getPow(pow / 2), powerhash[pow / 2 + 1],self.filas)
        return powerhash[pow]

    def transposeMatrix(self,m):
        t = []
        for r in range(len(m)):
            tRow = []
            for c in range(len(m[r])):
                if c == r:
                    tRow.append(m[r][c])
                else:
                    tRow.append(m[c][r])
            t.append(tRow)
        return t

    def getMatrixMinor(self,m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeternminant(self,m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(self,m):
        determinant = float(self.getMatrixDeternminant(m))
        # special case for 2x2 matrix:
        if (determinant != 0):
            if len(m) == 2:
                return [[round(float(m[1][1] / determinant),2), round(float(-1 * m[0][1] / determinant),2)],
                        [round(float(-1 * m[1][0] / determinant),2), round(float(m[0][0] / determinant),2)]]

            # find matrix of cofactors
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = self.getMatrixMinor(m, r, c)
                    cofactorRow.append(((-1) ** (r + c)) * float(self.getMatrixDeternminant(minor)))
                cofactors.append(cofactorRow)
            cofactors = self.transposeMatrix(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = round(float(cofactors[r][c] / determinant),2)
            return cofactors
        else:
            print ("no se puede")