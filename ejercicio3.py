#3) Elabore un programa para la facultad de Ingeniería que pida 400 números e indique si ese número es par o impar; 
# me muestre un listado y me indique cuantos son pares y cuantos son impares.

pares = 0                                                               # Inicializamos contadores par e impar
impares = 0

resultado = []                                                          # lista para almacenar los resultados



for i in range(1, 13 ):  
    numeros = int(input(f"Ingrese el número {i}: "))                    # Iteración  400 números al usuario

    if numeros % 2 == 0:                                                 # Condicional para verificar si es par o impar operador módulo (%) si el numero es divisible entre dos
        resultado.append(f" El Número {numeros} es par.")
        pares += 1                                                      # acumulador si entra por esta parte verdera del condicional- par
    else:
        resultado.append(f" El Número {numeros} es impar.")
        impares += 1                                                    # acumulador si entra por esta parte falsa del condicional- impar


for consolidado in resultado:                                           # Mostramos el listado de números y su clasificación
    print(consolidado)

print(f"Total de números pares: {pares}")                               # Mostramos cuántos son pares e impares
print(f"Total de números impares: {impares}")