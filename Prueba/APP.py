import os
import string

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Aplicación de Notas ---")
    print("1. Agregar una nota")
    print("2. Ver todas las notas")
    print("3. Eliminar una nota")
    print("4. Realizar análisis de datos")
    print("5. Salir")

# Función para agregar una nota
def agregar_nota(notas):
    nota = input("Escribe la nota: ")
    notas.append(nota)
    print("¡Nota agregada exitosamente!")

# Función para ver todas las notas
def ver_notas(notas):
    if notas:
        print("\nTus notas:")
        for idx, nota in enumerate(notas, 1):
            print(f"{idx}. {nota}")
    else:
        print("No tienes notas guardadas.")

# Función para eliminar una nota
def eliminar_nota(notas):
    ver_notas(notas)
    try:
        indice = int(input("¿Cuál nota deseas eliminar? (Ingresa el número): "))
        if 1 <= indice <= len(notas):
            removed = notas.pop(indice - 1)
            print(f"Nota '{removed}' eliminada.")
        else:
            print("Número de nota inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")

# Función para guardar las notas en un archivo
def guardar_notas(notas):
    with open("notas.txt", "w") as archivo:
        for nota in notas:
            archivo.write(nota + "\n")
    print("Notas guardadas correctamente.")

# Función para cargar las notas desde un archivo
def cargar_notas():
    if os.path.exists("notas.txt"):
        with open("notas.txt", "r") as archivo:
            return [nota.strip() for nota in archivo.readlines()]
    return []

# Función para analizar las notas
def analizar_datos(notas):
    if not notas:
        print("No hay notas para analizar.")
        return
    
    total_notas = len(notas)
    total_palabras = sum(len(nota.split()) for nota in notas)
    promedio_longitud = sum(len(nota) for nota in notas) / total_notas if total_notas > 0 else 0
    
    print("\n--- Análisis de Datos ---")
    print(f"Total de notas: {total_notas}")
    print(f"Total de palabras en todas las notas: {total_palabras}")
    print(f"Promedio de longitud de las notas: {promedio_longitud:.2f} caracteres")
    
    # Análisis de palabras más comunes (frecuencia de palabras)
    palabras = ' '.join(notas).lower()
    palabras = palabras.translate(str.maketrans('', '', string.punctuation))  # Eliminar puntuaciones
    palabras_lista = palabras.split()
    
    # Contar frecuencia de palabras
    from collections import Counter
    frecuencia_palabras = Counter(palabras_lista)
    
    # Mostrar las 5 palabras más comunes
    print("\nLas 5 palabras más comunes en las notas son:")
    for palabra, frecuencia in frecuencia_palabras.most_common(5):
        print(f"{palabra}: {frecuencia} veces")
    
# Función principal
def app_notas():
    notas = cargar_notas()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                agregar_nota(notas)
            elif opcion == 2:
                ver_notas(notas)
            elif opcion == 3:
                eliminar_nota(notas)
            elif opcion == 4:
                analizar_datos(notas)
            elif opcion == 5:
                guardar_notas(notas)
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida, por favor elige una opción entre 1 y 5.")
        except ValueError:
            print("Por favor ingresa un número válido.")

# Ejecutar la aplicación
if __name__ == "__main__":
    app_notas()