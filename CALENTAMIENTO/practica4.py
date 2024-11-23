print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#definir la fancion que dice si una letra es vocal o no
def caracter_vocal(a):
    if a in "aeiouAEIOU":
        return True
    else:
        return False
#Preguntar al usuario que ponga una letra
vocal=input("Coloca una letra: ")
caracter_vocal(vocal)
# Llamamos a la función y guardamos el resultado
if caracter_vocal(vocal):
    print(f"{vocal} es una vocal.")
else:
    print(f"{vocal} no es una vocal.")