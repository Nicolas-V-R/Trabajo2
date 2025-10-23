# 2- CONDICIONALES

import os
os.system('clear')

# Sentencias Condicionales (IF/ELIF/ELSE) 
age = 18

# La sintaxis usa dos puntos (:) y la indentación para definir el bloque de código 
if age >= 18:
    print("Eres mayor de edad.")
    print("Felicidades.")
elif age >= 16: 
    print("Casi eres mayor de edad.")
else:
    print("Eres menor de edad.") [52]


# Operadores Lógicos (and, or, not) 
has_license = True
has_money = False
age = 25

# AND (requiere que todas las condiciones sean True) 
if age >= 18 and has_license:
    print("Puedes conducir legalmente.")
else:
    print("Policía!")

# OR (requiere que al menos una condición sea True) 
if age > 60 or has_money:
    print("Tienes beneficios especiales.")
else:
    print("Sigue trabajando.")

# NOT (invierte el valor booleano) 
is_weekend = False
if not is_weekend:
    print("¡A trabajar!")

# Valores Truthy/Falsy 
# Números no cero, strings no vacíos, listas no vacías, etc., son considerados True en un contexto booleano.

if 5: # Evalúa a True
    print("El número no es cero.")

if "Juan": # Evalúa a True
    print("El nombre no está vacío.")

# 3. Condicionales Ternarios
# value_if_true if condition else value_if_false

status_message = "Mayor de edad" if age >= 18 else "Menor de edad"
print(status_message)

# 4. Operadores de Comparación 
print(1 == 1)  # Igualdad
print(1 != 2)  # Desigualdad
print(5 > 3)
print("Manzana" < "Pera") # Comparación lexicográfica (alfabética)
print("Hola" == "hola") # False (sensible a mayúsculas/minúsculas) 