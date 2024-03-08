```python
from datetime import datetime, timedelta

# Fecha actual
hoy = datetime.now()
print("Hoy es: ", hoy)

# Añadir 10 dias a la fecha actual
futuro = hoy + timedelta(days=10)
print("En 10 dias será: ", futuro)

# Si queremos restar 5 dias a la fecha actual
pasado = hoy - timedelta(days=5)
print("Hace 5 dias fue: ", pasado)

# Calcular la diferencia entre fechas

diferencia = futuro - hoy
print(f"La diferencia entre futuro y hoy es de: {diferencia.days} dias")

````