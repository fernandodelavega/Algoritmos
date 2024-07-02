def PadreAnadido(comics):
    orden = []
    visited = [False] * len(comics)

    while len(orden) != len(comics):
        for i in range(len(comics)):
            if not visited[i]:
                anadido = True
                cont = 0
                while anadido == True and cont < len(comics[i]):
                    if comics[i][cont] not in orden:
                        anadido = False
                    cont += 1
                if anadido:
                    orden.append(i)
                    visited[i] = True

    print(*orden)


nodos, relaciones = map(int, input().strip().split())

grafo = []

for _ in range(nodos):
    grafo.append([])

for _ in range(relaciones):
    u, v = map(int, input().strip().split())
    grafo[v].append(u)

PadreAnadido(grafo)
