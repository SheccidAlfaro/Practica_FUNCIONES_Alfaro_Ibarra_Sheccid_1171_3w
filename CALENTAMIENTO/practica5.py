print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#definir la funcion que suma la lista
def suma(lista):
    total = 0
    for num in lista:
        total += num
    return total
#definir la funcion que multiplica la lista
def multiplar(lista):
    total = 1
    for num in lista:
        total *= num
    return total

#Poner los datos
numeros = [5, 12, 3, 15, 21]
resultado_suma = suma(numeros)
resultado_multiplicacion = multiplar(numeros)
#mostrar el resultado de la suma y la multiplicacion
print("La suma es:", resultado_suma)  
print("La multiplicación es:", resultado_multiplicacion) 
