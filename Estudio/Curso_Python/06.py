# 6- REGEX

import os
import re # Módulo para Expresiones Regulares
os.system('clear')

# Usar prefijo 'r' para Raw String (Regex)

text = "Me gusta Python. Python no es tan difícil. Viva Python."
pattern_simple = r"Python"

# 1. re.search: Encuentra la primera ocurrencia 
match = re.search(pattern_simple, text)

if match:
    # Match object [144]
    print(f"Patrón encontrado: {match.group()}") # El texto encontrado 
    print(f"Inicia en posición: {match.start()}") # Índice de inicio 
    print(f"Termina en posición: {match.end()}") # Índice de fin (excluyente) 
else:
    print("Patrón no encontrado.")

# 2. re.findall: Devuelve una lista de todas las coincidencias 
matches_list = re.findall(pattern_simple, text)
print(f"Todas las coincidencias: {matches_list}")

# 3. Modificador IGNORECASE (Ignora mayúsculas/minúsculas)
pattern_ia = r"ia"
text_ia = "Todo el mundo habla de la IA y el trabajo."
matches_case = re.findall(pattern_ia, text_ia, re.IGNORECASE)
print(f"Coincidencias de 'IA' (sin distinción): {matches_case}")

# 4. re.sub: Reemplazar coincidencias 
new_text = re.sub(r"Hola", "Adiós", "Hola Mundo. Hola de nuevo.")
print(f"Texto reemplazado: {new_text}")

# Metacaracteres y Cuantificadores
text_metachar = "Mi número es 688123. Mi email es test@gmail.com."

# Metacaracteres 
# Coincide con cualquier carácter (excepto salto de línea)
print(re.findall(r"M. ", text_metachar)) # Busca M, cualquier caracter, espacio

# \d : Coincide con cualquier dígito (0-9) 
# \w : Coincide con alfanuméricos (letras, números, _)
# \s : Coincide con espacio en blanco (espacio, tabulación, salto de línea) 
# ^ : Coincide con el inicio de la cadena 
# $ : Coincide con el final de la cadena 
# \. : Busca el punto literal (escapando el significado especial) 

# Cuantificadores (Repetición) 
# + : Una o más veces 
# {n} : Exactamente n veces 
# {n,m} : Entre n y m veces 
# {n,} : n o más veces 

# Ejemplo de patrón para 3 dígitos 
print(re.findall(r"\d{3}", text_metachar)) 

# Sets (Conjuntos) 
# [aeiou] : Coincide con una vocal 
print(re.findall(r"[aeiou]", "murcielago")) # Todas las vocales
# [^aeiou] : Niega el conjunto (coincide con cualquier cosa que no sea vocal) 
# [a-z] : Rango (cualquier minúscula) 