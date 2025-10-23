# 3- LISTAS

import os
os.system('clear')

# Creación y Acceso a Listas 
list_one = [1, 65-68]
list_two = ["manzanas", "peras", "plátanos"]
list_mix = [10, "texto", 3.14, True] # Listas pueden contener diferentes tipos 
list_empty = []

# Acceso por índice (inicia en 0)
print(list_two) # 'manzanas'

# Acceso por índice negativo (desde el final) 
print(list_two[-1]) # 'plátanos' (último elemento)
print(list_two[-2]) # 'peras' (penúltimo)

# Listas anidadas (matrices) 
list_of_lists = [[1, 65], [66, 67]]
print(list_of_lists[1]) # Accede a 3

# 2. Slicing (Rebanado) 
# Sintaxis: [inicio:fin:paso]. El índice 'fin' es excluyente 

# Desde el índice 1 hasta antes del 4 (elementos 2, 3, 4) 
slice_list = list_one[1:4] 
print(slice_list) 

# Desde el inicio hasta antes del índice 3 (elementos 1, 2, 3) 
print(list_one[:3]) 

# Desde el índice 2 hasta el final 
print(list_one[2:]) 

# Copia completa de la lista 
copy_list = list_one[:]

# Slicing con paso (Step) 
print(list_one[::2]) 

# Invertir lista usando slicing
print(list_one[::-1]) 

# 3. Modificación y Longitud 
list_one = 20 # Modificar elemento 
print(list_one) 

# Concatenación (menos eficiente, crea nueva lista)
list_one = list_one + [82, 83]

# Concatenación más eficiente
list_one += [85, 86]

# Longitud de la lista (usando la función len()) 
print(f"Longitud de list_one: {len(list_one)}")

# 4. Métodos de Lista (`.append`, `.insert`, `.remove`, etc.)
list_three = ['a', 'b', 'c']

# Agregar al final 
list_three.append('d') 

# Insertar en una posición específica (empuja elementos a la derecha) 
list_three.insert(1, '@') 

# Agregar varios elementos de otro iterable 
list_three.extend(['e', 'f'])

# Eliminar primera aparición de un elemento (por valor) 
list_three.remove('@') 

# Eliminar y devolver el último elemento
last_element = list_three.pop() 
print(f"Elemento eliminado: {last_element}")

# Eliminar por índice (y devuelve el elemento) 
element_at_index_one = list_three.pop(1) 

# Eliminar por rango o índice (sin devolver el elemento) 
del list_three 

# Ordenar listas 
numbers = [65, 66, 85, 99]
numbers.sort() # Ordena in-place (modifica la original)
print(f"Lista ordenada (modificada): {numbers}")

# Crear una nueva lista ordenada (la original no se modifica) 
unsorted_numbers = [65, 66, 99]
sorted_new = sorted(unsorted_numbers)
print(f"Nueva lista ordenada: {sorted_new}. Original: {unsorted_numbers}")