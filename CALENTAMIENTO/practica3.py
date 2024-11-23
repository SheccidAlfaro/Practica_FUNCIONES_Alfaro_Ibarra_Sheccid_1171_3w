print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#definir la funcion
def cal_long(o):
    #utilizar un ciclo for
    contador = 0
    for _ in o:
        contador += 1
    return contador

# Solicitar al usuario que ingrese una lista y una cadena
lista_input = input("Colocar una lista (separada por comas): ")
cadena_input = input("Colocar una cadena: ")

# Convertir la entrada de la lista en una lista real
lista = lista_input.split(',')

# Calcular la longitud de la lista y la cadena
longitud_lista = cal_long(lista)
longitud_cadena = cal_long(cadena_input)

# Mostrar los resultados
print(f"La longitud de la lista es: {longitud_lista}")
print(f"La longitud de la cadena es: {longitud_cadena}")
