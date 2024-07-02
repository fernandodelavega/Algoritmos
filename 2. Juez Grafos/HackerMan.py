from collections import deque
def dfs(node, g, visited):
    q = deque()
    visited[node] = True
    q.append(node)
    while q:
        aux = q.popleft()
        for neighbor in g[aux]:
            if not visited[neighbor]:
                #dfs(neighbor, visited)
                visited[neighbor] = True
                q.append(neighbor)

def find_connected_components(g, primero):
    visited = [False] * n
    visited[0] = primero;
    components_count = 0
    for node in range(n):
        if not visited[node]:
            dfs(node, g, visited)
            components_count += 1
    return components_count

n, m = map(int, input().strip().split())
w = []
g = []

for _ in range (n):
    num = int(input().strip())
    w.append(num)
    g.append([])
for _ in range (m):
    u, v = map(int, input().strip().split())
    g[u].append(v)
    g[v].append(u)

auxg = []
coste = 0
#print (w)

for i in range(len(g)):
    auxg = g[i]
    g[i] = []
    #print (g)
    if i == 0:
        components_count = find_connected_components(g, True)
    else:
        components_count = find_connected_components(g, False)
    if components_count > 1:
        coste += w[i]
    g[i] = auxg

print(coste)