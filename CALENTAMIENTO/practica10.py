print("")
print("Alfaro_Ibarra_Sheccid_practica")
print("")
def histograma(numeros):
    # Determinar el valor máximo para la escala del histograma
    max_valor = max(numeros) if numeros else 0
    
    # Imprimir el histograma
    for numero in numeros:
        # Crear la línea del histograma: el número seguido de corazones
        corazon = '♥' * numero
        print(f"{numero}: {corazon}")


numeros = [2, 2, 8, 3, 4]
histograma(numeros)
