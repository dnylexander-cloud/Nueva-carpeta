filas = 4
columnas = 4

M1 = [[0 for j in range(columnas)] for i in range(filas)]
M2 = [[0 for j in range(columnas)] for i in range(filas)]
MR = [[0 for j in range(columnas)] for i in range(filas)]

print("Ingrese los elementos de la matriz 1:")
for i in range(filas):
    for j in range(columnas):
        M1[i][j] = int(input("Ingrese el elemento de la matriz 1 en la posición " + str(i) + "," + str(j) + ": "))

print("\nAhora ingrese los elementos de la segunda matriz\n")
for i in range(filas):
    for j in range(columnas):
        M2[i][j] = int(input("Ingrese el elemento de la matriz 2 en la posición " + str(i) + "," + str(j) + ": "))

print("\nMATRIZ 1\n")
for renglones in M1:
    print(*renglones)

print("\nMATRIZ 2\n")
for renglones in M2:
    print(*renglones)

print("\nMATRIZ RESULTANTE DE LA SUMA\n")
for i in range(filas):
    for j in range(columnas):
        MR[i][j] = M1[i][j] + M2[i][j]

for renglones in MR:
    print(*renglones)

print("\nMATRIZ RESULTANTE DE LA MULTIPLICACION\n")
# ===== Multiplicación de las matrices =====
for i in range(filas):
    for j in range(columnas):
        suma = 0
        for k in range(columnas):  # o filas_B, son iguales
            suma += M1[i][k] * M2[k][j]
        MR[i][j] = suma

for renglones in MR:
    print(*renglones)
