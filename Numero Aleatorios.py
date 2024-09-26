def centros_al_cuadrado(seed, n, d):
    resultados = []
    num = seed

    for _ in range(n):
        # Elevar el número al cuadrado
        cuadrado = num ** 2
        
        # Convertir a string y rellenar con ceros si es necesario
        cuadrado_str = str(cuadrado).zfill(2 * d)
        
        # Extraer los dígitos centrales
        start = (len(cuadrado_str) - d) // 2
        num_str_centro = cuadrado_str[start:start + d]
        
        # Convertir de nuevo a número entero
        num = int(num_str_centro)
        resultados.append(num)
    
    return resultados


def medios_al_cuadrado(seed1, seed2, n, d):
    resultados = []
    num1 = seed1
    num2 = seed2

    for _ in range(n):
        # Multiplicar las dos semillas
        producto = num1 * num2
        
        # Convertir el producto a string y rellenar con ceros si es necesario
        producto_str = str(producto).zfill(2 * d)
        
        # Extraer los dígitos centrales
        start = (len(producto_str) - d) // 2
        num_str_centro = producto_str[start:start + d]
        
        # Convertir de nuevo a número entero
        nuevo_num = int(num_str_centro)
        resultados.append(nuevo_num)
        
        # Actualizar las semillas para la siguiente iteración
        num1 = num2
        num2 = nuevo_num
    
    return resultados


semilla_centro = 6759  
semilla1 = 2456        
semilla2 = 3421        
digitos = 4            
n = 100                

centros = centros_al_cuadrado(semilla_centro, n, digitos)
print("Método de Centros al Cuadrado:", centros)

medios = medios_al_cuadrado(semilla1, semilla2, n, digitos)
print("Método de Medios al Cuadrado:", medios)


