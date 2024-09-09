v = 1023.4
print("Volumen", v , "metros cubicos")
print("Volumen {0:.4f} metros cubicos".format(v))

x = 1
if x > 0 :
    print("Positivo")
else:
    print("Negativo")
    
print("#" * 15)
for x in [3, 4.25, "Hola", True] :
    print(x)
print("#" * 15)
for x in range(5, -10, -2)  :
    print(x)

import CodClases.funciones as fun
array = [[1,2,3], [4,5,6], [7,8,9]]
fun.calcularSumaArray(array)
