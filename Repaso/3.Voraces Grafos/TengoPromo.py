def prim(nodo, arrL):
    visitados = set()
    distMin = [float("inf") for i in range(len(arrL))]
    distMin[nodo] = 0

    while len(visitados) != len(arrL):
        dist = float("inf")
        actual = -1

        for indexnodo in range(len(distMin)):
            if distMin[indexnodo] < dist and indexnodo not in visitados:
                dist = distMin[indexnodo]
                actual = indexnodo
        for i in range(len(arrL[actual])):
            d = arrL[actual][i][1]
            d += distMin[actual]
            distMin[arrL[actual][i][0]] =min(d, distMin[arrL[actual][i][0]])
        visitados.add(actual)

    return distMin

def salida(tipo, distancias,tiposL):
    miniM = float("inf")
    for nodo in tiposL[tipo]:
        if
    #if distancia minima del nodo es menor que miniM  -> minimM = distanciaminimi

    return

Nodos, Caminos = map(int, input().strip().split())
T = list(map(int, input().strip().split()))

tipo = {}
for i in range(max(T) + 1):
    tipo[i] = []
for i in range(len(T)):
    tipo[T[i]].append(i)

arr = [[] for _ in range(Nodos)]
for _ in range(Caminos):
    c, d, l = map(int, input().strip().split())
    arr[c].append([d, l])
    arr[d].append([c, l])

dist = {}
for i in range(Nodos):
    dist[i] = prim(i, arr)
output  = ""
for _ in range(len(tipo)):
    output = output + str(salida(_,dist,tipo)) + " "

print(output.strip())