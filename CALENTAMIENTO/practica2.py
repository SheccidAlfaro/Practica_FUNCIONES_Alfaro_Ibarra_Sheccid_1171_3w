print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
#definir funcion con sus argumentos para saber que numero es mayor
def max(a, b, c):
    #Utilizar if para saber cual es mayor
    if a>b:
        print(f"{a} es mayor que {b} y {c}")
    elif b>a:
        print(f"{b} es mayor que {a} y {b}")
    elif c>a and c>b:
        print(f"{c} es mayor que {a} y {b}")
    else:
        print("no valido")
#Llamar a la funcion 
max(9,4,7)