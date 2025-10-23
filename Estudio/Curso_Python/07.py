# 7- FECHAS 

from datetime import datetime, timedelta # Módulo nativo
import locale
import os
os.system('clear')

# Configurar locale para mostrar meses/días en español 
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    # Intento fallback si es necesario
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES')
    except locale.Error:
        print("Advertencia: No se pudo configurar el locale en español.")

# 1. Fecha y hora actual [167]
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Fecha y hora específica (Año, Mes, Día, Hora, Minuto, Segundo) 
specific_date = datetime(2025, 2, 12, 15, 30, 0) # 12 de Febrero de 2025
print(f"Fecha específica: {specific_date}")

# 3. Acceder a componentes individuales 
print(f"Año actual: {now.year}")
print(f"Mes actual: {now.month}")

# 4. Formatear fechas (usando strftime y directivas %) 
# %A: Nombre del día de la semana, %B: Nombre del mes, %d: Día, %Y: Año, %H: Hora, %M: Minuto
formatted_date = now.strftime("%A, %d de %B de %Y")
print(f"Fecha formateada: {formatted_date}")

# 5. Operaciones con Fechas (timedelta) 
# timedelta representa una duración o diferencia de tiempo 

# Fecha de ayer 
yesterday = now - timedelta(days=1)
print(f"Ayer fue: {yesterday}")

# Una hora después 
one_hour_later = now + timedelta(hours=1)
print(f"En una hora será: {one_hour_later}")

# También se pueden usar fracciones (ej: half_day=0.5) 
half_day_ago = now - timedelta(days=0.5) 
print(f"Hace medio día: {half_day_ago}")

# 6. Diferencia entre dos fechas 
diff = specific_date - now
print(f"Diferencia (timedelta): {diff}")
print(f"Días de diferencia: {diff.days}")