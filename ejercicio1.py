#1) Elabore un programa para la Universidad de Florida que calcule los primeros 
#100 números de la siguiente serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.
# la serie suma el primero numero mas el segundo y eso te da el tercer numero de la serie

numprimero = 5                                      # Inicializamos los primeros dos números de la serie
numsegundo = 8
serie = []                                          # Creamos una lista para almacenar los números de la serie

"""for _ in range(100):                                # 100 iteraciones
    if numprimero != 13:                            # Si num1 no es 13, lo agregamos a la lista
        serie.append(numprimero)
    
    siguiente_numero = numprimero + numsegundo      # Calculamos el siguiente número en la serie
    numprimero = numsegundo                         # Actualizamos num1 y num2
    numsegundo = siguiente_numero

print(serie)                                        # Mostramos la lista de la serie
"""

while len(serie) < 100:                             # Usamos un bucle while para generar los 100 números
    if numprimero != 13:                            
        serie.append(numprimero)    
    
    siguiente_numero = numprimero + numsegundo      
    numprimero = numsegundo                         
    numsegundo = siguiente_numero                

print(serie)  