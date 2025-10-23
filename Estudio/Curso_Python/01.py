#FUNDAMENTOS

# Importar módulos necesarios (ejemplo para limpiar consola)
import os

# Función para limpiar la terminal (utiliza el comando 'clear' del sistema) [14]
def limpiar_terminal():
    os.system('clear')

# Ejecutar la limpieza al inicio para una salida clara [14]
limpiar_terminal()

# --- 1. Salida de Datos (Función print) --- [15]
print("Hola mundo")  # Uso de comillas dobles
print('Hola Python')  # Uso de comillas simples [16]

# Imprimir múltiples valores separados por coma (por defecto usa espacio como separador) [17]
print("Manzana", "Pera", "Plátano")

# Configurar el separador (SEP) [18]
print("Python", "es", "brutal", sep="-")

# Configurar el final de línea (END) (por defecto es un salto de línea) [19, 20]
print("Esto se imprime", end=" ")
print("en una línea")

# --- 2. Variables y Tipado --- [21, 22]
# Python es de tipado Dinámico (el tipo puede cambiar en tiempo de ejecución) [22, 23]
# Y de tipado Fuerte (no realiza conversiones automáticas entre tipos incompatibles) [24]

my_name = "midudep" # String
age = 32 # Entero (int)

# Reasignación de valor y cambio de tipo (Dinámico) [22, 25]
age = 39.5 # Flotante (float)

# F-Strings (Cadenas Literales Formateadas) [24, 26]
print(f"Hola {my_name}, tu edad actual es {age} años.")
print(f"Tu edad en 5 años será: {age + 5}")

# Constantes (solo por convención, no son inmutables) [27]
PI_VALUE = 3.14159
# PI_VALUE = 2 # Esto es posible, pero no recomendado [28]

# Anotaciones de tipo (solo para ayuda del editor/herramientas, no para Python en ejecución) [29, 30]
is_active: bool = True
user_name: str = "Guido"

# Comentarios [31, 32]
# Comentario de una línea
"""
Esto es un docstring
o un comentario multilínea
(usualmente usado para documentación)
"""

# --- 3. Tipos de Datos Básicos y Casting --- [33]
print(type(10)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("texto")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'> [34]

# Conversión de Tipos (Casting) [35-37]
number_str = "100"
number_int = int(number_str) # Convierte string a entero
print(number_int + 2) # 102 (Suma exitosa)

# Conversión de float a int (trunca el decimal, no redondea) [37, 38]
print(int(3.99)) # 3
print(round(3.99)) # 4 (Función de redondeo real) [39]

# Conversión a Booleano (0 es False, todo lo demás, incluyendo -1, es True) [37]
print(bool(0)) # False
print(bool(-1)) # True
print(bool("")) # False (Cadena vacía es False) [40]
print(bool(" ")) # True (Cadena con espacio es True) [40]

# --- 4. Entrada de Datos (Input) --- [41]
# El input siempre devuelve una cadena de texto (str) [42]
name = input("Hola ¿cómo te llamas? ")
print(f"Hola {name}, encantado de conocerte.")

# Se requiere casting para operar con números [42, 43]
try:
    age_input = int(input("¿Cuántos años tienes? "))
    print(f"Dentro de 20 años tendrás {age_input + 20} años.")
except ValueError:
    print("Error: Debes introducir un número válido.") [44, 45]

# Obtener múltiples valores (requiere split) [46, 47]
try:
    country, city = input("¿En qué país y ciudad vives (separados por espacio)? ").split()
    print(f"Vives en {city}, {country}.")
except ValueError:
    print("Error: Introduce el país y la ciudad separados por un espacio.")