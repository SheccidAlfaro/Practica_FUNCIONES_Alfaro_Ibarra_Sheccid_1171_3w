print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#Definir una funcion que tome dos listas com argumentos
#y diga true si hay un elemento similar en ambas listas y false si no hay elementos similares
#con bucle for
def comparar_listas(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

#poner las dos listas
lista1 = ["Arroz", "Frijoles", "Papas"]
lista2 = ["Chile", "Papas", "Cebolla"]
#Llamar a la funcion
print(comparar_listas(lista1, lista2))  

