# 1- FUNDAMENTOS

# Importar módulos necesarios (ejemplo para limpiar consola)
import os

# Función para limpiar la terminal (utiliza el comando 'clear' del sistema) 
def limpiar_terminal():
    os.system('clear')

# Ejecutar la limpieza al inicio para una salida clara 
limpiar_terminal()

# 1. Salida de Datos (Función print) 
print("Hola mundo") 
print('Hola Python') 

# Imprimir múltiples valores separados por coma (por defecto usa espacio como separador) 
print("Manzana", "Pera", "Plátano")

# Configurar el separador (SEP)
print("Python", "es", "brutal", sep="-")

# Configurar el final de línea (END) (por defecto es un salto de línea) 
print("Esto se imprime", end=" ")
print("en una línea")

# 2. Variables y Tipado 
# Python es de tipado Dinámico (el tipo puede cambiar en tiempo de ejecución) 
# Y de tipado Fuerte (no realiza conversiones automáticas entre tipos incompatibles) 

my_name = "midudep" # String
age = 32 # Entero (int)

# Reasignación de valor y cambio de tipo (Dinámico) 
age = 39.5 # Flotante (float)

# F-Strings (Cadenas Literales Formateadas) 
print(f"Hola {my_name}, tu edad actual es {age} años.")
print(f"Tu edad en 5 años será: {age + 5}")

# Constantes (solo por convención, no son inmutables) 
PI_VALUE = 3.14159
# PI_VALUE = 2 # Esto es posible, pero no recomendado 

# Anotaciones de tipo (solo para ayuda del editor/herramientas, no para Python en ejecución) 
is_active: bool = True
user_name: str = "Guido"

# Comentarios 
# Comentario de una línea
"""
Esto es un docstring
o un comentario multilínea
(usualmente usado para documentación)
"""

# 3. Tipos de Datos Básicos y Casting 
print(type(10)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("texto")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'> 

# Conversión de Tipos (Casting) 
number_str = "100"
number_int = int(number_str) 
print(number_int + 2)

# Conversión de float a int (trunca el decimal, no redondea) 
print(int(3.99)) # 3
print(round(3.99)) # 4 (Función de redondeo real) 

# Conversión a Booleano (0 es False, todo lo demás, incluyendo -1, es True) 
print(bool(0)) # False
print(bool(-1)) # True
print(bool("")) # False (Cadena vacía es False)
print(bool(" ")) # True (Cadena con espacio es True) 

# 4. Entrada de Datos (Input) 
# El input siempre devuelve una cadena de texto (str) 
name = input("Hola ¿cómo te llamas? ")
print(f"Hola {name}, encantado de conocerte.")

# Se requiere casting para operar con números 
try:
    age_input = int(input("¿Cuántos años tienes? "))
    print(f"Dentro de 20 años tendrás {age_input + 20} años.")
except ValueError:
    print("Error: Debes introducir un número válido.") [44, 45]

# Obtener múltiples valores (requiere split) 
try:
    country, city = input("¿En qué país y ciudad vives (separados por espacio)? ").split()
    print(f"Vives en {city}, {country}.")
except ValueError:
    print("Error: Introduce el país y la ciudad separados por un espacio.")