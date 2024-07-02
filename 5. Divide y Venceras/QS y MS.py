def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return combinar(left, right)


def combinar(izquierda, derecha):
    resultado = []
    i, j = 0, 0

    # Combina elementos de izquierda y derecha
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Añade los elementos restantes de izquierda o derecha
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


array = list(map(int, input().strip().split()))  # Lista de elementos a ordenar
x = mergesort(array)
print(x)  # Lista ordenada
