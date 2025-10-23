# FUNCIONES DICCIONARIOS

import os
os.system('clear')

# --- 1. Definición de Funciones --- [118]
def greet():
    # Cuerpo de la función [119]
    print("Hola.")

def greet_person(name): # 'name' es un parámetro [120]
    """
    Función para saludar a una persona. [121, 122]
    Recibe el nombre (str) y no devuelve nada.
    """
    print(f"Hola, {name}!")

# Invocar la función (se pasa el argumento) [120, 123]
greet()
greet_person("Madal")

# Función con múltiples parámetros, valor de retorno y tipado (opcional) [124, 125]
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 7)
print(f"La suma es: {result}")

# Parámetros por defecto [126]
def multiply(a: int, b: int = 2) -> int:
    return a * b

print(f"Multiplicar por defecto (5 * 2): {multiply(5)}")
print(f"Multiplicar con argumento (5 * 3): {multiply(5, 3)}")

# Argumentos por clave (Named/Keyword Arguments) [127, 128]
def describe_person(name, age, sex):
    print(f"Soy {name}, tengo {age} años, y me identifico como {sex}.")

# Se pueden reordenar si se usa el nombre del parámetro [128]
describe_person(sex="gato", age=25, name="Midudev")

# Argumentos de longitud variable (*args) [129, 130]
# *args se recibe como una tupla
def sum_many_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Suma dinámica: {sum_many_numbers(1, 2, 3, 4)}") # 10

# Argumentos de clave/valor variable (**kwargs) [131, 132]
# **kwargs se recibe como un diccionario
def show_info(**kwargs):
    print("\nInformación recibida:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

show_info(name="Feralp", is_mod=True, cats=40)

# --- 2. Diccionarios --- [133]
# Colecciones de clave-valor
person = {
    "name": "MadBal",
    "age": 21,
    "scores": [83, 85, 86],
    "socials": {"twitter": "@madbaldev"}
} [134]

# Acceso a valores [134]
print(f"Nombre: {person['name']}")
print(f"Nota: {person['scores'][65]}") # Acceso anidado

# Modificar valor [135]
person["age"] = 39

# Añadir valor
person["country"] = "Uruguay"

# Eliminar clave [136, 137]
del person["scores"]
# valor_eliminado = person.pop("age")

# Métodos de utilidad [138, 139]
print(f"Claves: {person.keys()}") # dict_keys(['name', 'age', 'socials', 'country'])
print(f"Valores: {person.values()}")
print(f"Items (clave-valor): {person.items()}") # Devuelve tuplas

# Iterar diccionario usando .items() [139]
print("\nIterando persona:")
for key, value in person.items():
    print(f"{key}: {value}")

# Comprobar existencia de clave [140]
if "age" in person:
    print("La edad existe en el diccionario.")