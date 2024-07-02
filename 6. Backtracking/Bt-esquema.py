def vuelta_atras(v, k, opciones, es_solucion, es_prometedor):
    """
    Procedimiento general de backtracking (vuelta atrás).

    Parámetros:
    - v: Lista de valores que representa la solución actual que se está construyendo.
    - k: Tamaño actual de la solución v.
    - opciones: Lista de valores disponibles para elegir.
    - es_solucion: Función que verifica si v[1..k] es una solución completa.
    - es_prometedor: Función que verifica si v[1..k] es prometedora.

    """
    # Verifica si v[1..k] es una solución completa
    if es_solucion(v, k):
        # Procesar la solución (en este caso, la imprimimos)
        print("Solución encontrada:", v[:k])
    else:
        # Explora cada posible valor en opciones
        for ei in opciones:
            # Establece el siguiente elemento de la solución
            v[k] = ei
            # Verifica si la solución parcial v[1..k+1] es prometedora
            if es_prometedor(v, k):
                # Llama recursivamente a vuelta_atras con k+1
                vuelta_atras(v, k + 1, opciones, es_solucion, es_prometedor)

# Ejemplo de uso:

# Define las funciones es_solucion y es_prometedor para el problema específico

def es_solucion(v, k):
    # Verifica si v[1..k] es una solución completa
    # En este caso, verificamos si se ha completado la solución para un tamaño específico
    return k == 3  # Por ejemplo, queremos una solución de longitud 3

def es_prometedor(v, k):
    # Verifica si v[1..k] es prometedora
    # En este caso, podemos verificar si la solución parcial es válida o no
    # Por ejemplo, no permitimos números repetidos
    return len(set(v[:k])) == k

# Lista de valores disponibles para elegir
opciones = [1, 2, 3, 4]

# Lista para almacenar la solución actual (tamaño máximo igual a la longitud de opciones)
v = [0] * len(opciones)

# Llamada inicial al procedimiento de vuelta atrás
vuelta_atras(v, 0, opciones, es_solucion, es_prometedor)

