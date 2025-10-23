#CONDICIONALES

import os
os.system('clear')

# Sentencias Condicionales (IF/ELIF/ELSE) [2, 48]
age = 18

# La sintaxis usa dos puntos (:) y la indentación para definir el bloque de código [49, 50]
if age >= 18:
    print("Eres mayor de edad.")
    print("Felicidades.")
elif age >= 16: # Elif es 'else if' [51]
    print("Casi eres mayor de edad.")
else:
    print("Eres menor de edad.") [52]


# Operadores Lógicos (and, or, not) [53-55]
has_license = True
has_money = False
age = 25

# AND (requiere que todas las condiciones sean True) [53]
if age >= 18 and has_license:
    print("Puedes conducir legalmente.")
else:
    print("Policía!")

# OR (requiere que al menos una condición sea True) [54, 56]
if age > 60 or has_money:
    print("Tienes beneficios especiales.")
else:
    print("Sigue trabajando.")

# NOT (invierte el valor booleano) [55]
is_weekend = False
if not is_weekend:
    print("¡A trabajar!")

# Valores Truthy/Falsy [57]
# Números no cero, strings no vacíos, listas no vacías, etc., son considerados True en un contexto booleano.

if 5: # Evalúa a True
    print("El número no es cero.")

if "Juan": # Evalúa a True
    print("El nombre no está vacío.")

# --- 3. Condicionales Ternarios --- [58, 59]
# value_if_true if condition else value_if_false

status_message = "Mayor de edad" if age >= 18 else "Menor de edad"
print(status_message)

# --- 4. Operadores de Comparación --- [60]
print(1 == 1)  # Igualdad
print(1 != 2)  # Desigualdad
print(5 > 3)
print("Manzana" < "Pera") # Comparación lexicográfica (alfabética) [61, 62]
print("Hola" == "hola") # False (sensible a mayúsculas/minúsculas) [63]