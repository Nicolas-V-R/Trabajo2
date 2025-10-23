# 5- FUNCIONES DICCIONARIOS

import os
os.system('clear')

# 1. Definición de Funciones
def greet():
    # Cuerpo de la función
    print("Hola.")

def greet_person(name): # 'name' es un parámetro 
    """
    Función para saludar a una persona. [121, 122]
    Recibe el nombre (str) y no devuelve nada.
    """
    print(f"Hola, {name}!")

# Invocar la función (se pasa el argumento)
greet()
greet_person("Madal")

# Función con múltiples parámetros, valor de retorno y tipado (opcional) 
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 7)
print(f"La suma es: {result}")

# Parámetros por defecto 
def multiply(a: int, b: int = 2) -> int:
    return a * b

print(f"Multiplicar por defecto (5 * 2): {multiply(5)}")
print(f"Multiplicar con argumento (5 * 3): {multiply(5, 3)}")

# Argumentos por clave (Named/Keyword Arguments) 
def describe_person(name, age, sex):
    print(f"Soy {name}, tengo {age} años, y me identifico como {sex}.")

# Se pueden reordenar si se usa el nombre del parámetro 
describe_person(sex="gato", age=25, name="Midudev")

# Argumentos de longitud variable (*args) 
# *args se recibe como una tupla
def sum_many_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Suma dinámica: {sum_many_numbers(1, 2, 3, 4)}") # 10

# Argumentos de clave/valor variable (**kwargs) 
# **kwargs se recibe como un diccionario
def show_info(**kwargs):
    print("\nInformación recibida:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

show_info(name="Feralp", is_mod=True, cats=40)

# 2. Diccionarios 
# Colecciones de clave-valor
person = {
    "name": "MadBal",
    "age": 21,
    "scores": [83, 85, 86],
    "socials": {"twitter": "@madbaldev"}
} [134]

# Acceso a valores 
print(f"Nombre: {person['name']}")
print(f"Nota: {person['scores'][65]}") # Acceso anidado

# Modificar valor 
person["age"] = 39

# Añadir valor
person["country"] = "Uruguay"

# Eliminar clave 
del person["scores"]
# valor_eliminado = person.pop("age")

# Métodos de utilidad 
print(f"Claves: {person.keys()}") # dict_keys(['name', 'age', 'socials', 'country'])
print(f"Valores: {person.values()}")
print(f"Items (clave-valor): {person.items()}") # Devuelve tuplas

# Iterar diccionario usando .items() 
print("\nIterando persona:")
for key, value in person.items():
    print(f"{key}: {value}")

# Comprobar existencia de clave 
if "age" in person:
    print("La edad existe en el diccionario.")