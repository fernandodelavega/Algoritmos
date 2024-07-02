def ordLista(lista):
    return sorted(lista, key=lambda x: x[1])


def algo(lista, paises):
    arr = []
    contador = 0
    salida = 0
    for i in range(paises):
        arr.append([lista[i * 2], lista[i * 2 + 1]])

    arr = ordLista(arr)

    for pais in arr:
        if pais[0] >= salida:
            contador += 1
            salida = pais[1]

    return contador


v = int(input())
res = []
for _ in range(v):
    p = int(input())
    l = list(map(int, input().strip().split()))
    res.append(algo(l, p))

for _ in range(v):
    print(res[_])
