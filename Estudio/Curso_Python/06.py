#REGEX

import os
import re # Módulo para Expresiones Regulares [141]
os.system('clear')

# Usar prefijo 'r' para Raw String (Regex) [142]

text = "Me gusta Python. Python no es tan difícil. Viva Python."
pattern_simple = r"Python"

# 1. re.search: Encuentra la primera ocurrencia [143]
match = re.search(pattern_simple, text)

if match:
    # Match object [144]
    print(f"Patrón encontrado: {match.group()}") # El texto encontrado [144]
    print(f"Inicia en posición: {match.start()}") # Índice de inicio [145]
    print(f"Termina en posición: {match.end()}") # Índice de fin (excluyente) [145]
else:
    print("Patrón no encontrado.")

# 2. re.findall: Devuelve una lista de todas las coincidencias [146]
matches_list = re.findall(pattern_simple, text)
print(f"Todas las coincidencias: {matches_list}")

# 3. Modificador IGNORECASE (Ignora mayúsculas/minúsculas) [147, 148]
pattern_ia = r"ia"
text_ia = "Todo el mundo habla de la IA y el trabajo."
matches_case = re.findall(pattern_ia, text_ia, re.IGNORECASE)
print(f"Coincidencias de 'IA' (sin distinción): {matches_case}")

# 4. re.sub: Reemplazar coincidencias [149]
new_text = re.sub(r"Hola", "Adiós", "Hola Mundo. Hola de nuevo.")
print(f"Texto reemplazado: {new_text}")

# --- Metacaracteres y Cuantificadores ---
text_metachar = "Mi número es 688123. Mi email es test@gmail.com."

# Metacaracteres [150]
# . : Coincide con cualquier carácter (excepto salto de línea) [150]
print(re.findall(r"M. ", text_metachar)) # Busca M, cualquier caracter, espacio

# \d : Coincide con cualquier dígito (0-9) [151]
# \w : Coincide con alfanuméricos (letras, números, _) [152]
# \s : Coincide con espacio en blanco (espacio, tabulación, salto de línea) [153]
# ^ : Coincide con el inicio de la cadena [154]
# $ : Coincide con el final de la cadena [155]
# \. : Busca el punto literal (escapando el significado especial) [151]

# Cuantificadores (Repetición) [156]
# + : Una o más veces [157]
# {n} : Exactamente n veces [158]
# {n,m} : Entre n y m veces [159]
# {n,} : n o más veces [160]

# Ejemplo de patrón para 3 dígitos [161]
print(re.findall(r"\d{3}", text_metachar)) # ['688', '123']

# Sets (Conjuntos) [162]
# [aeiou] : Coincide con una vocal [163]
print(re.findall(r"[aeiou]", "murcielago")) # Todas las vocales
# [^aeiou] : Niega el conjunto (coincide con cualquier cosa que no sea vocal) [164]
# [a-z] : Rango (cualquier minúscula) [165]