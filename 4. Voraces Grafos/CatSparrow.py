from queue import PriorityQueue

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, start))
    predecessors = [-1] * n

    while pq:
        dist, node = pq.get()
        if visited[node]:
            continue
        visited[node] = True
        if node == end:
            break
        for neighbor in graph[node]:
            if not visited[neighbor[1]]:
                new_dist = dist + neighbor[2]
                if new_dist < distances[neighbor[1]]:
                    distances[neighbor[1]] = new_dist
                    predecessors[neighbor[1]] = node
                    pq.put((new_dist, neighbor[1]))

    # Reconstruir el camino desde el nodo final hasta el inicial
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    return distances[end], path

n, m = map(int, input().strip().split())
g = []
for i in range(n):
    g.append([])
for i in range(m):
    u, v, d = map(int, input().strip().split())
    g[u].append((u, v, d))
    g[v].append((v, u, d))
s, e = map(int, input().strip().split())

shortest_distance, shortest_path = dijkstra(g, s, e)
print(shortest_distance)
print(" ".join(map(str, shortest_path)))
