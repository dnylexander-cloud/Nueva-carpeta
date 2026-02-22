filas = 4
columnas = 4
def leer(nombre):
    print("\nIngrese los elementos de la matriz", nombre)
    M = [[0 for j in range(columnas)] for i in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            M[i][j] = int(input("Elemento en posición " + str(i) + "," + str(j) + ": "))
    return M
def resultado(M, nombre):
    print("\n" + nombre)
    for renglon in M:
        print(*renglon)


def sumar(M1, M2):
    MR = [[0 for j in range(columnas)] for i in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            MR[i][j] = M1[i][j] + M2[i][j]
    return MR



def multiplicar(M1, M2):
    MR = [[0 for j in range(columnas)] for i in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            suma = 0
            for k in range(columnas):
                suma += M1[i][k] * M2[k][j]
            MR[i][j] = suma
    return MR


M1 = leer("1")
M2 = leer("2")

resultado(M1, "MATRIZ 1")
resultado(M2, "MATRIZ 2")

MR_suma = sumar(M1, M2)
resultado(MR_suma, "MATRIZ RESULTANTE DE LA SUMA")

MR_mult = multiplicar(M1, M2)
resultado(MR_mult, "MATRIZ RESULTANTE DE LA MULTIPLICACION")