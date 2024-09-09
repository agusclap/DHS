def leerDatos():
    with open('nombres.txt','r') as reader:
        for line in reader.readlines():
            print(line, end='\n')
leerDatos()

def convertirDatos():
    numeros = []
    with open('numeros.txt','r') as reader:
        for num in reader.readlines():
            numeros.append(num)
    return numeros

lista = convertirDatos()
for line in lista:
    print(line)        
    
def convertirDatosLambda(entrada):
    # Leemos el contenido del archivo y dividimos por líneas
    with open(entrada, 'r') as archivo:
        # Utilizamos una lista por comprensión para convertir cada línea a entero
        return [int(linea.strip()) for linea in archivo if linea.strip().isdigit()]

datos = convertirDatosLambda('numeros.txt')
print(datos)

def noRepetidos(datos):
    count = 0
    lista_noRepeat = []
    
    while count < len(datos):
        # Contamos la cantidad de veces que aparece el elemento en la lista
        if datos.count(datos[count]) == 1:
            # Si aparece solo una vez, lo agregamos a la lista de no repetidos
            lista_noRepeat.append(datos[count])
            print("agregado")
        else:
            print("repetido")
        
        count += 1  # Incrementa el contador

    return lista_noRepeat

# Ejemplo de uso
lista1 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6]  # Lista de ejemplo
lista2 = noRepetidos(lista1)
print(lista2)  # Salida esperada: [2, 4, 6]
      
    