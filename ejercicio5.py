#5) Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable, 
# registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, 
# si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.

# Número de cabinas
num_cabinas = int(input(f"Ingresa el número de cabinas "))                                    # Número de cabinas

resultados = []                                                                               # Lista para almacenar los resultados de cada cabina

for i in range(1, num_cabinas + 1):                                                           # Ciclo para registrar el puntaje de cada cabina y clasificar su funcionamiento
    puntaje = int(input(f"Ingrese el puntaje de la cabina {i} (2, 3 o 4): "))
    
    if puntaje == 2:                                                                          # condicional para Clasificación según el puntaje
        clasificacion = "Funcionamiento defectuoso"
    elif puntaje == 3:
        clasificacion = "Funcionamiento moderado"
    elif puntaje == 4:
        clasificacion = "Funcionamiento óptimo"
    else:
        clasificacion = "Puntaje fuera de rango"

    resultados.append(f"La Cabina {i}: {clasificacion}")                                          # Guardar el resultado de la cabina

for resultado in resultados:                                                                   # Mostrar la clasificación de cada cabina
    print(resultado)