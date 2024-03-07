from datetime import datetime
# Estructura de datos para almacenar los eventos
eventos = []

def registrar_eventos(nombre, fecha, descripcion):
    for evento in eventos:
        if evento['nombre'] == nombre and evento['fecha'] == fecha:
            print("Ya existe un evento con este nombre y con la misma fecha!")
            return
    eventos.append({"nombre": nombre, "fecha": fecha, "descripcion": descripcion})
    print("Evento registrado con éxito")