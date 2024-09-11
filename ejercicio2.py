#2)	Elabore un programa para el Éxito que determine el salario de los 1897 empleados de su compañía, 
#teniendo en cuenta las comisiones y la seguridad social que debe pagar, e imprima el listado de la información. 


num_empleados = int(input(f"Ingresa el número de empleados: "))                                # inicializar variable

empleados = []                                                                                 # Lista para almacenar la info empleados

for i in range(1, num_empleados + 1):                                                          # Ciclo para calcular el salario de cada empleado
    salario_base = float(input(f"Ingresa el salario base del empleado {i}: "))
    comision = float(input(f"Ingresa la comisión del empleado {i}: "))

    seguridad_social = salario_base * 0.08                                                     # Seguridad social (8% del salario base)

    
    salario_total = salario_base + comision - seguridad_social                                 # Salario total (salario base + comisiones - seguridad social)

    
    empleado = {                                                                                # Guardar la info del empleado en un diccionario y agregar a la lista
        'empleado_id': i,
        'salario_base': salario_base,
        'comision': comision,
        'seguridad_social': seguridad_social,
        'salario_total': salario_total
    }
    empleados.append(empleado)

for empleado in empleados:                                                                      # Mostrar el listado de empleados con su información
    print(f"Empleado {empleado['empleado_id']}:")
    print(f"  Salario Base: {empleado['salario_base']}")
    print(f"  Comisión: {empleado['comision']}")
    print(f"  Seguridad Social: {empleado['seguridad_social']}")
    print(f"  Salario Total: {empleado['salario_total']}")
    print("*****************************************************")