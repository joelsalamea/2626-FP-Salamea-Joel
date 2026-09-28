"""Ejercicio de colecciones: registro de estudiantes y notas.

Este programa permite almacenar la información de los estudiantes de la
Unidad Educativa Ayapamba utilizando un diccionario. Además, incluye
funcionalidades para agregar, buscar, eliminar y mostrar registros.
"""

# Diccionario principal: nombre del estudiante -> nota
estudiantes = {
    "Ana": 9.5,
    "Luis": 8.7,
    "Mateo": 7.8,
    "Sofía": 9.1,
}


def agregar_estudiante():
    """Agrega un nuevo estudiante con su nota al diccionario."""
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if nombre in estudiantes:
        print(f"El estudiante {nombre} ya existe. Use la opción de actualizar nota.")
        return

    try:
        nota = float(input("Ingrese la nota del estudiante: "))
    except ValueError:
        print("La nota debe ser un número válido.")
        return

    estudiantes[nombre] = nota
    print(f"Estudiante {nombre} agregado con nota {nota}.")


def mostrar_estudiantes():
    """Muestra toda la información almacenada en pantalla."""
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\nLista de estudiantes y notas:")
    for nombre, nota in estudiantes.items():
        print(f"- {nombre}: {nota}")


def buscar_estudiante():
    """Busca un estudiante y muestra su nota."""
    nombre = input("Ingrese el nombre a buscar: ").strip().title()
    if nombre in estudiantes:
        print(f"{nombre} tiene una nota de: {estudiantes[nombre]}")
    else:
        print(f"No se encontró al estudiante {nombre}.")


def actualizar_nota():
    """Actualiza la nota de un estudiante existente."""
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if nombre not in estudiantes:
        print(f"El estudiante {nombre} no existe.")
        return

    try:
        nueva_nota = float(input("Ingrese la nueva nota: "))
    except ValueError:
        print("La nota debe ser un número válido.")
        return

    estudiantes[nombre] = nueva_nota
    print(f"La nota de {nombre} fue actualizada a {nueva_nota}.")


def eliminar_estudiante():
    """Elimina un estudiante del diccionario."""
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"El estudiante {nombre} fue eliminado.")
    else:
        print(f"No se encontró al estudiante {nombre}.")


def calcular_promedio():
    """Calcula el promedio de las notas de todos los estudiantes."""
    if not estudiantes:
        print("No hay datos para calcular el promedio.")
        return

    promedio = sum(estudiantes.values()) / len(estudiantes)
    print(f"El promedio general de notas es: {promedio:.2f}")


def mostrar_menu():
    """Muestra el menú principal del programa."""
    print("\n=== Sistema de registro de estudiantes ===")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar nota")
    print("5. Eliminar estudiante")
    print("6. Calcular promedio")
    print("7. Salir")


def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            actualizar_nota()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "6":
            calcular_promedio()
        elif opcion == "7":
            print("Gracias por usar el sistema de notas de la Unidad Educativa Ayapamba.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
