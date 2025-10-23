#LISTAS

import os
os.system('clear')

# Creación y Acceso a Listas [3, 64]
list_one = [1, 65-68]
list_two = ["manzanas", "peras", "plátanos"]
list_mix = [10, "texto", 3.14, True] # Listas pueden contener diferentes tipos [64]
list_empty = []

# Acceso por índice (inicia en 0) [69]
print(list_two) # 'manzanas'

# Acceso por índice negativo (desde el final) [70]
print(list_two[-1]) # 'plátanos' (último elemento)
print(list_two[-2]) # 'peras' (penúltimo)

# Listas anidadas (matrices) [71, 72]
list_of_lists = [[1, 65], [66, 67]]
print(list_of_lists[1]) # Accede a 3

# --- 2. Slicing (Rebanado) --- [73]
# Sintaxis: [inicio:fin:paso]. El índice 'fin' es excluyente [74]

# Desde el índice 1 hasta antes del 4 (elementos 2, 3, 4) [73, 74]
slice_list = list_one[1:4] 
print(slice_list) # [65-67]

# Desde el inicio hasta antes del índice 3 (elementos 1, 2, 3) [75]
print(list_one[:3]) # [1, 65, 66]

# Desde el índice 2 hasta el final [76]
print(list_one[2:]) # [66-68]

# Copia completa de la lista [76]
copy_list = list_one[:]

# Slicing con paso (Step) [77, 78]
print(list_one[::2]) # [1, 66, 68] (índices 0, 2, 4)

# Invertir lista usando slicing [79, 80]
print(list_one[::-1]) # [1, 65-68]

# --- 3. Modificación y Longitud ---
list_one = 20 # Modificar elemento [80]
print(list_one) # [10, 65-68]

# Concatenación (menos eficiente, crea nueva lista) [81]
list_one = list_one + [82, 83]

# Concatenación más eficiente [84]
list_one += [85, 86]

# Longitud de la lista (usando la función len()) [87]
print(f"Longitud de list_one: {len(list_one)}")

# --- 4. Métodos de Lista (`.append`, `.insert`, `.remove`, etc.) --- [88, 89]
list_three = ['a', 'b', 'c']

# Agregar al final [90]
list_three.append('d') # ['a', 'b', 'c', 'd']

# Insertar en una posición específica (empuja elementos a la derecha) [91]
list_three.insert(1, '@') # ['a', '@', 'b', 'c', 'd']

# Agregar varios elementos de otro iterable [92]
list_three.extend(['e', 'f'])

# Eliminar primera aparición de un elemento (por valor) [93]
list_three.remove('@') # ['a', 'b', 'c', 'd', 'e', 'f']

# Eliminar y devolver el último elemento [94]
last_element = list_three.pop() # 'f'
print(f"Elemento eliminado: {last_element}")

# Eliminar por índice (y devuelve el elemento) [95]
element_at_index_one = list_three.pop(1) # 'b'

# Eliminar por rango o índice (sin devolver el elemento) [96, 97]
del list_three # Elimina 'a'

# Ordenar listas [98]
numbers = [65, 66, 85, 99]
numbers.sort() # Ordena in-place (modifica la original) [100]
print(f"Lista ordenada (modificada): {numbers}")

# Crear una nueva lista ordenada (la original no se modifica) [100]
unsorted_numbers = [65, 66, 99]
sorted_new = sorted(unsorted_numbers)
print(f"Nueva lista ordenada: {sorted_new}. Original: {unsorted_numbers}")