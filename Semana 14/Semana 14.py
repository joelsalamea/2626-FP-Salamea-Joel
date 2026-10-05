# Área de un rectángulo

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def main():
    print("Calculadora de área de un rectángulo")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")

if __name__ == "__main__":
    main()
