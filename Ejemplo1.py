tareas = []

def agregar_tarea(nombre, responsable):
    tarea = {
        "nombre": nombre,
        "responsable": responsable,
        "estado": "Pendiente"
    }
    tareas.append(tarea)
    print("Tarea agregada correctamente")

def mostrar_tareas():
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea['nombre']} - {tarea['responsable']} - {tarea['estado']}")

agregar_tarea("Diseñar material educativo", "Diseñador instruccional")
agregar_tarea("Revisar contenido final", "Revisor")

mostrar_tareas()