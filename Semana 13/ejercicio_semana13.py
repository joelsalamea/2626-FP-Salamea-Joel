# Pseudocódigo:
# 1. Definir función calcular_area_rectangulo(base, altura)
# 2. Calcular area = base * altura
# 3. Retornar area
# 4. En bloque principal, llamar a la función con valores de ejemplo y mostrar resultado


def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dados la base y la altura.
    Parámetros:
        base (float): longitud de la base
        altura (float): longitud de la altura
    Retorna:
        float: área del rectángulo
    """
    area = base * altura
    return area


if __name__ == "__main__":
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
    except ValueError:
        print("Entrada inválida. Por favor ingrese números válidos para base y altura.")
    else:
        resultado = calcular_area_rectangulo(base, altura)
        print(f"Área del rectángulo (base={base}, altura={altura}): {resultado}")
