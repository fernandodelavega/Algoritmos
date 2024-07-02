from queue import PriorityQueue

def read_input():
    n, m,alegTime = map(int, input().strip().split())
    g = []
    for i in range(n):
        g.append([])
    for i in range(m):
        u,v,d = map(int, input().strip().split())
        g[u].append((v, d))
        g[v].append((u, d))
    return g,alegTime


def dijkstra(g):
    n = len(g)
    dist = [float("Inf")] * n # Mostrar todas las distancias a un número muy grande
    pq = PriorityQueue()      # Cola de prioridad por distancias menores
    dist[0] = 0               # El primer nodo siempre es el 0 se marca a 0
    pq.put((0,0))             # Se añade en la cola de prioridad para comenzar a buscar la distancia
    while not pq.empty():
        u = pq.get()          # Sacamos el primer nodo que tenga menor distancia
        for v in g[u[1]]:
            alt = dist[u[1]] + v[1]     # Sumamos su distancia junto a la de ir al nodo destino
            if alt < dist[v[0]]:        # Si es menor significa que hay un camino mejor y no entra
                dist[v[0]] = alt        # Se establece la distancia menor
                pq.put((alt, v[0]))     # Se mete en la cola de prioridad para expandir sus nodos

    return dist               # Devuelve la matriz de distancia final

g,alegTime = read_input()
dist = dijkstra(g)
#print(dist)
res = sum(dist)
#print(res)

if sum(dist)<=alegTime:
    print(res)
else:
    print("Aleg, a decorar!")

