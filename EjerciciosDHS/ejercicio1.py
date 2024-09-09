from random import randint


def generarDatos(n):
    numeros = []
    for x in range(n):
        num = randint(0,100)
        numeros.append(num)
    return numeros
p = 5
random = []
random = generarDatos(p)
for y in range(len(random)):
    print(random[y],"")
           
    
# Definir los datos como una lista de tuplas
names = [("Agustin", 1), ("Damian", 2), ("Juan", 3), ("Santino", 4), ("Alvaro", 5)]

def guardarDatos(datos):
    # Abrir el archivo en modo escritura
    with open('datos.txt', 'w') as file:
        # Recorrer cada tupla de datos
        for nombre, numero in datos:
            # Escribir cada nombre y número en una línea del archivo
            file.write(f"{nombre},{numero}\n")

guardarDatos(names)
