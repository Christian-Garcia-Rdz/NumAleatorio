import random

numeros_aleatorios = [random.random() for _ in range(100)]

print("Números aleatorios generados:")
print(numeros_aleatorios)

def prueba_uniformidad(numeros, num_intervalos):
    intervalos = [0] * num_intervalos
    total_numeros = len(numeros)

    for num in numeros:
        index = int(num * num_intervalos)
        if index == num_intervalos:
            index -= 1
        intervalos[index] += 1

    frecuencia_esperada = total_numeros / num_intervalos

    estadistico = sum(((observada - frecuencia_esperada) ** 2) / frecuencia_esperada for observada in intervalos)

    return estadistico

num_intervalos = 10
estadistico = prueba_uniformidad(numeros_aleatorios, num_intervalos)

valor_critico = 16.92  # Aproximado para 9 grados de libertad

# Mostrar los resultados de la prueba
print("\nResultado de la prueba de uniformidad:")
print(f"Estadístico calculado: {estadistico:.4f}")
print(f"Valor crítico (con 0.05 de significancia): {valor_critico}")
