#4) 4)	 Elabore un programa para un Hospital que determine, y muestre 
# el nivel de Leucemia de 803 pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia; 
# si esta entre 11 y 40, nivel bajo de Leucemia; 
# si esta entre 40 y 69, nivel moderado de Leucemia, 
# si esta entre 70 y 100, nivel grave de Leucemia


num_pacientes = int(input(f"Ingresa el número de pacientes "))                               # Número de pacientes

resultados = []                                                                              # Lista para almacenar los resultados

for i in range(1, num_pacientes + 1):                                                        # Ciclo para solicitar y clasificar el nivel de leucemia de cada paciente
    puntaje = float(input(f"Ingrese el puntaje de leucemia del paciente {i}: "))

    if puntaje < 10:                                                                         # Condicional para saber la Clasificación según el puntaje
        clasificacion = "No tiene leucemia"
    elif 11 <= puntaje <= 40:
        clasificacion = "Nivel bajo de leucemia"
    elif 41 <= puntaje <= 69:
        clasificacion = "Nivel moderado de leucemia"
    elif 70 <= puntaje <= 100:
        clasificacion = "Nivel grave de leucemia"
    else:
        clasificacion = "Puntaje fuera de rango"

    resultados.append(f"Paciente {i}: {clasificacion}")                                      # Guardar el resultado del paciente


for resultado in resultados:                                                                 # Mostrar la clasificación de cada paciente
    print(resultado)