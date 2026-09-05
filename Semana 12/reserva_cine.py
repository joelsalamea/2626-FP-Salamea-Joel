1# Programa para gestionar la reserva de butacas en una sala de cine.
# La sala se representa como una matriz (lista de listas) de 3 filas por 4 columnas.

# Se crea la matriz con valores iniciales en 0.
# Las filas válidas son 0, 1 y 2, y las columnas válidas son 0, 1, 2 y 3.
sala = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir al usuario una única fila y columna para reservar una butaca (marca 1).
try:
    fila = int(input("Ingrese la fila a reservar (0-2): "))
    columna = int(input("Ingrese la columna a reservar (0-3): "))
    if not (0 <= fila < 3) or not (0 <= columna < 4):
        print("Fila o columna fuera de rango. Debe ingresar fila 0-2 y columna 0-3.")
    else:
        if sala[fila][columna] != 0:
            print("La butaca ya está reservada.")
        else:
            sala[fila][columna] = 1
            print(f"Butaca en fila {fila}, columna {columna} reservada.")
except ValueError:
    print("Entrada inválida. Ingrese números enteros para fila y columna.")

# Se muestra el estado actual de la sala recoriendo la matriz con bucles anidados.
print("\nEstado de la sala:")
for fila in range(3):
    for columna in range(4):
        print(sala[fila][columna], end=" ")
    print()
