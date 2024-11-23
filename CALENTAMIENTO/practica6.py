print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#Definir una funcion que haga que una cadena de texto sea invertida
def invertir_cadena(cadena):
    return cadena[::-1]

#Preguntar al usuario que coloque una cadena de texto
cadena = input("Coloque una cadena de texto: ")
#Llamar a la funcion invertir_cadena y mostrar el resultado
print("La cadena invertida es: ", invertir_cadena(cadena))

