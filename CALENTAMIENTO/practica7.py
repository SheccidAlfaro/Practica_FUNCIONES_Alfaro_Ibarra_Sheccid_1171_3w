print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
def palabra_palindromo(palabra):
    #si la palabra es igual a la palabra al reves, es palindromo
    return palabra == palabra[::-1]
#Preguntar al usuario si quiere ingresar una palabra
pl=input("Pon una palabra: ")
#utilizar if para saber si la palabra es palindromo o no
if  palabra_palindromo (pl):
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")