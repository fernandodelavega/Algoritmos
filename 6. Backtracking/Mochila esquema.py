# Esquema general mochila
def mochila_va(i, r, v, w, memo):
    """
    Calcula el máximo valor que se puede obtener utilizando los elementos de índice i al n
    y cuyo peso total no exceda r.

    Parámetros:
    - i: Índice actual desde el que se consideran los elementos.
    - r: Peso restante que se puede usar para seleccionar elementos.
    - v: Lista de valores de los elementos.
    - w: Lista de pesos de los elementos.
    - memo: Diccionario para memoización (almacena resultados de subproblemas).

    Retorna:
    - El máximo valor posible que se puede obtener.
    """
    # Verifica si ya existe el resultado en memoización
    if (i, r) in memo:
        return memo[(i, r)]

    # Si i es igual a la longitud de la lista de valores, ya no hay elementos que considerar
    if i == len(v):
        return 0

    # Inicializa b (valor máximo obtenido) en 0
    b = 0

    # Itera a través de los elementos desde i hasta el final de la lista
    for k in range(i, len(v)):
        # Verifica si el peso del elemento k es menor o igual a r
        if w[k] <= r:
            # Calcula el valor total obtenido al agregar el elemento k y realizar la llamada recursiva
            # con k y el peso restante r - w[k]
            valor = v[k] + mochila_va(k, r - w[k], v, w, memo)
            # Actualiza b si el valor calculado es mayor que el valor actual de b
            b = max(b, valor)

    # Almacena el resultado en memoización
    memo[(i, r)] = b

    # Devuelve el valor máximo obtenido
    return b

# Ejemplo de uso:
v = [60, 100, 120]  # Lista de valores de los elementos
w = [10, 20, 30]    # Lista de pesos de los elementos
r = 50              # Peso máximo permitido

# Inicializa un diccionario para memoización
memo = {}

# Llama a la función mochila_va con los valores iniciales (i=0, r=r, v=v, w=w, memo=memo)
max_valor = mochila_va(0, r, v, w, memo)

print(f"El valor máximo que se puede obtener es: {max_valor}")


