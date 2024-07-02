from collections import deque


def funcion(listaA, listaB, nodes):
    # visitados = [False] * nodes
    solucion = [-1] * nodes
    cola = deque()

    # calculo nodos origen
    for i in range(len(listaA)):
        if not listaA[i]:
            solucion[i] = 0
            cola.append(i)

    while cola:
        actual = cola.popleft()
        # visitados[actual] = True

        for nodo in listaB[actual]:
            cola.append(nodo)
            solucion[nodo] = solucion[actual] + 1

    return solucion


Nodos, Caminos = map(int, input().strip().split())
arr, arr2 = [], []

for _ in range(Nodos):
    arr.append([])
    arr2.append([])

for _ in range(Caminos):
    H1, H2 = map(int, input().strip().split())
    arr[H2].append(H1)
    arr2[H1].append(H2)
C = int(input().strip())

sol = funcion(arr, arr2, Nodos)

for _ in range(C):
    P1, P2 = map(int, input().strip().split())

    if sol[P1] < sol[P2]:
        print("Menor rango", end="\n")
    elif sol[P1] > sol[P2]:
        print("Mayor rango", end="\n")
    else:
        print("Rango similar", end="\n")
