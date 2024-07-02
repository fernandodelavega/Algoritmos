def Fans(grafo, nota):
    visited = [False] * len(grafo)
    nodosARecorer = []
    nodosRecorridos = []

    nodosARecorer.append(0)
    nodosRecorridos.append(0)
    visited[0] = True

    for k in range(nota - 1):
        nodosPorRecorrer = nodosARecorer
        nodosARecorer = []
        for nodo in nodosPorRecorrer:
            for adj in grafo[nodo]:
                if not visited[adj]:
                    visited[adj] = True
                    nodosARecorer.append(adj)
                    nodosRecorridos.append(adj)

    return len(nodosRecorridos)


nCon = int(input().strip())

grafo = []
notas = []

for n in range(nCon):
    grafo.append([])
    nota, nodos, conexiones = map(int, input().strip().split())
    notas.append(nota)

    for _ in range(nodos):
        grafo[n].append([])

    for i in range(conexiones):
        u, v = map(int, input().strip().split())
        grafo[n][u].append(v)
        grafo[n][v].append(u)

for j in range(nCon):
    print(Fans(grafo[j], notas[j]))
