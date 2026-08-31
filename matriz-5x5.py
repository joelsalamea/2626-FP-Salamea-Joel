matriz = [[0 for _ in range(5)] for _ in range(5)]

# Lectura de datos con validación
for i in range(5):
    for j in range(5):
        while True:
            try:
                valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
                matriz[i][j] = valor
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero válido.")

# Impresión de la matriz en consola
print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()