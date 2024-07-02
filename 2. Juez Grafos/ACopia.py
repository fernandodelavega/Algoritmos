from collections import defaultdict

def minimum_Groups(N, M, L):
    # Create an adjacency list representation of the graph

    adj_list = defaultdict(list)

    for u, v in L:
        adj_list[u].append(v)

        adj_list[v].append(u)

    # Initialize the visited set and the result list

    visited = set()

    result = []

    # Perform a depth-first search to find the minimum number of groups

    for node in range(N):

        if node not in visited:

            group = []

            stack = [node]

            while stack:

                current_node = stack.pop()

                if current_node not in visited:
                    visited.add(current_node)

                    group.append(current_node)

                    stack.extend(adj_list[current_node])

            result.append(group)

    return result


# Read the input

Nodes, Conexions = map(int, input().split())

listConexions = []

for i in range(Conexions):
    U, V = map(int, input().split())

    listConexions.append([U, V])

# Obtener el resultado

result = minimum_Groups(Nodes, Conexions, listConexions)

# Imprimir el resultado

print(len(result))
