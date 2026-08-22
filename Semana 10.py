# Declaración de la matriz de 3x3
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Recorrido e impresión de la matriz mediante ciclos anidados
print("Contenido de la matriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Posición [{i}][{j}]: {matriz[i][j]}")