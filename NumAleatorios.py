import random

# Generar 100 números aleatorios entre 0 y 1 usando la función random
numeros_aleatorios = [random.random() for _ in range(100)]

# Mostrar los números generados
print("Números aleatorios generados:")
print(numeros_aleatorios)

# Función para calcular la frecuencia observada en intervalos
def prueba_uniformidad(numeros, num_intervalos):
    # Dividir el rango [0, 1) en 'num_intervalos' partes iguales
    intervalos = [0] * num_intervalos
    total_numeros = len(numeros)

    # Contar cuántos números caen en cada intervalo
    for num in numeros:
        index = int(num * num_intervalos)
        if index == num_intervalos:
            index -= 1
        intervalos[index] += 1

    # Calcular la frecuencia esperada
    frecuencia_esperada = total_numeros / num_intervalos

    # Comparar frecuencias observadas y esperadas
    estadistico = sum(((observada - frecuencia_esperada) ** 2) / frecuencia_esperada for observada in intervalos)

    return estadistico

# Realizar la prueba de uniformidad usando la distribución de Chi-Cuadrado
num_intervalos = 10
estadistico = prueba_uniformidad(numeros_aleatorios, num_intervalos)

# Valor crítico de Chi-Cuadrado con (k-1) grados de libertad, para k=10 intervalos y nivel de significancia 0.05
valor_critico = 16.92  # Aproximado para 9 grados de libertad

# Mostrar los resultados de la prueba
print("\nResultado de la prueba de uniformidad:")
print(f"Estadístico calculado: {estadistico:.4f}")
print(f"Valor crítico (con 0.05 de significancia): {valor_critico}")
