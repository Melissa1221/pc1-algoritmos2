# Método de Fuerza Bruta
def moda_fuerza_bruta(arr):
    max_freq = 0
    moda = None
    
    for i in range(len(arr)):
        freq = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                freq += 1
                
        if freq > max_freq:
            max_freq = freq
            moda = arr[i]
    
    return moda

# Método Divide y Vencerás (con diccionario)
def moda_divide_y_venceras(arr):
    frecuencias = {}
    
    # Contar las frecuencias
    for num in arr:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    
    # Encontrar la moda
    max_freq = 0
    moda = None
    for num, freq in frecuencias.items():
        if freq > max_freq:
            max_freq = freq
            moda = num
    
    return moda

# Ejemplo de ejecución
arr = [3, 1, 2, 3, 4, 3, 2]

print("Moda (Fuerza Bruta):", moda_fuerza_bruta(arr))
print("Moda (Divide y Vencerás):", moda_divide_y_venceras(arr))


import time
import random

# Generar un vector aleatorio
def generar_vector(n):
    return [random.randint(0, 100) for _ in range(n)]

# Medir el tiempo de ejecución
def medir_tiempo(funcion, arr):
    inicio = time.time()
    funcion(arr)
    fin = time.time()
    return fin - inicio

# Probar con diferentes tamaños de vector
tamaños = [100, 1000, 10000, 100000]
resultados = []

for n in tamaños:
    arr = generar_vector(n)
    
    tiempo_fuerza_bruta = medir_tiempo(moda_fuerza_bruta, arr)
    tiempo_divide_venceras = medir_tiempo(moda_divide_y_venceras, arr)
    
    resultados.append([n, tiempo_fuerza_bruta, tiempo_divide_venceras])

# Guardando los resultados en un archivo de texto
with open('resultados_moda.txt', 'w') as f:
    f.write("Tamaño del vector\tFuerza Bruta (s)\tDivide y Vencerás (s)\n")
    for resultado in resultados:
        f.write(f"{resultado[0]}\t{resultado[1]:.6f}\t{resultado[2]:.6f}\n")

print("Los resultados han sido guardados en 'resultados_moda.txt'")
