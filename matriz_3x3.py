"""
Parte 1: Programa con matriz
Declara una matriz de 3x3 con números enteros.
Recorre la matriz utilizando ciclos.
Imprime todos los valores de la matriz en pantalla.
"""

# Definir matriz como arreglo de 3x3
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Recorrer la matriz usando ciclos anidados
print("Valores de la matriz 3x3:")
print()

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()  # Nueva línea después de cada fila
