def func(peñaL, coneL):
    visitados = [False] * len(peñaL)
    ncc = 0

    for nodo in peñaL:
        visitados[nodo] = True


    return


a, b, Equipo = map(str, input().strip().split())
Nodos = int(a)
Caminos = int(b)
peña = []
conexiones = []
for i in range(Nodos):
    c = input().strip()
    if c == Equipo:
        peña.append(i)


for _ in range(Caminos):
    x, y = map(int, input().strip().split())
    if x in peña and y in peña:
        conexiones.append([x, y])


print(func(peña, conexiones))
