from datetime import datetime, timedelta
# Estructura de datos para almacenar los eventos
eventos = []

def registrar_eventos(nombre, fecha, descripcion):
    for evento in eventos:
        if evento['nombre'] == nombre and evento['fecha'] == fecha:
            print("Ya existe un evento con este nombre y con la misma fecha!")
            return
    eventos.append({"nombre": nombre, "fecha": fecha, "descripcion": descripcion})
    print("Evento registrado con éxito")

def notificar_eventos_proximos():
    hoy = datetime.now().date()
    limite = hoy + timedelta(days=3)

    eventos_proximos = [evento for evento in eventos if hoy <= evento['fecha'] <= limite]

    if eventos_proximos:
        print("Eventos proximos")
        for evento in eventos_proximos:
            print(f"{evento['nombre']} - {evento['fecha']}: {evento['descripcion']}")
    else:
        print("No hay eventos próximos en los siguientes 3 días")

registrar_eventos("Concierto de Imagine Dragons ", datetime(2024, 3, 7).date(), "Concierto en vivo apertura del tour 2024")
registrar_eventos("Conferencia de Python", datetime(2024, 3, 10).date(), "Aprende las novedades de python para este 2024")
notificar_eventos_proximos()