# Abrir el archivo y leer todas las líneas con codificación 'latin-1'
with open("registro_temperatura365d_smn.txt", "r", encoding='latin-1') as file:
    # Leer todas las líneas del archivo excluyendo las primeras tres líneas
    lines = file.readlines()[3:]

# Crear un diccionario para almacenar los datos
datos = {}

# Procesar cada línea del archivo
for line in lines:
    parts = line.split()
    if len(parts) >= 4:
        fecha, tmax, tmin, estacion = parts[:4]

        if estacion not in datos:
            datos[estacion] = {"tmax": [], "tmin": []}

        # Si no hay registro de temperatura, almacenar como None
        tmax = float(tmax) if tmax.replace(".", "", 1).isdigit() else None
        tmin = float(tmin) if tmin.replace(".", "", 1).isdigit() else None

        datos[estacion]["tmax"].append(tmax)
        datos[estacion]["tmin"].append(tmin)

# Función para buscar la estación de manera insensible a mayúsculas/minúsculas
def buscar_estacion(nombre_buscar):
    for estacion in datos:
        if estacion.lower() == nombre_buscar.lower():
            return estacion
    return None

# Imprimir todas las temperaturas mínimas hace 3 días junto con la estación correspondiente
for estacion, data in datos.items():
    temp_min_estacion = data["tmin"][3] if len(data["tmin"]) > 3 else None
    if temp_min_estacion is not None:
        print(f"Estación: {estacion}, Temperatura mínima hace 3 días: {temp_min_estacion} grados Celsius")
    else:
        print(f"Estación: {estacion}, No hay datos de temperatura mínima hace 3 días")