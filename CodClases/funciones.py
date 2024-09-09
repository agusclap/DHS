def sumatoria(x, y):
    return x + y;
x = 2;
y = -2;
print(sumatoria(x,y))
array = [[1,2,3], [4,5,6], [7,8,9]]
def calcularSumaArray(array):
    count = 0
    suma = 1
    i = 0
    for fila in array:
        for i in fila:
            suma += i;
            count = count + 1
    
    print("-" * 15)
    print("Resultado =", suma, "En", count, "iteraciones" )

#calcularSumaArray(array)