# 4- BUCLES

import os
os.system('clear')

# 1. Bucle While
counter = 0

while counter <= 5: # Condición de bucle
    print(f"Contador: {counter}")
    # Se debe actualizar la condición para evitar un bucle infinito 
    counter += 1

# Bucle infinito (solo un ejemplo) 
# while True:
#     print("Hola") # Se ejecuta para siempre si no se rompe

# Bucle While con BREAK 
counter = 0
while True:
    counter += 1
    if counter == 5:
        print("Saliendo del bucle en 5...")
        break # Rompe el bucle inmediatamente 
    if counter > 6:
        break

# Bucle While con CONTINUE 
# Muestra solo números impares
print("\nBucle con Continue (Impares):")
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0: # Si es par
        continue # Salta esta iteración y va a la siguiente
    print(counter)

# Bucle While con ELSE 
# El bloque 'else' se ejecuta si el bucle termina normalmente (la condición while es False) 
# NO se ejecuta si el bucle se rompe con 'break' 
counter = 0
while counter < 3:
    print(f"Contando: {counter}")
    counter += 1
else:
    print("El bucle terminó normalmente.")

# 2. Bucle For y Range
fruits = ["manzana", "pera", "mandarina"]

# Iterar sobre una lista 
print("\nIterando frutas:")
for fruit in fruits:
    print(fruit)

# Range (secuencia/rango de números, no crea una lista en memoria) 
# range(fin) -> de 0 a fin-1
# range(inicio, fin)
# range(inicio, fin, paso)
print("\nNúmeros del 0 al 4 (range(5)):")
for i in range(5):
    print(i) # 0, 1, 2, 3, 4

# Range con inicio, fin, y paso 
print("\nNúmeros pares del 0 al 10:")
for i in range(0, 10, 2):
    print(i) # 0, 2, 4, 6, 8

# Iterar N veces (se usa '_' si la variable no se va a usar) 
for _ in range(3):
    print("Repitiendo acción 3 veces.")

# For con Enumerate (para obtener índice y valor) 
print("\nÍndice y Valor:")
for index, item in enumerate(fruits):
    print(f"Índice {index}: {item}")

# List Comprehension (Comprensión de Listas) 
# Forma concisa de crear listas: [expresión for item in iterable if condición]
list_numbers = [1, 65-68, 82]
# Crear lista de números pares [
even_numbers = [num for num in list_numbers if num % 2 == 0]
print(f"Números pares: {even_numbers}") 