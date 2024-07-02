def btEnemigos(N, M, enemies, array, X, Y, moves, visited, defeatedEnemies, directions):
    if enemies == defeatedEnemies:
        return "ATACA"
    elif moves <= 0:
        return "CORRE"
    else:
        for dir in directions:
            new_posX, new_posY = X + dir[0], Y + dir[1]

            if (0 <= new_posX < N) and (0 <= new_posY < M) and (array[new_posX][new_posY] != -1) and (
                    (new_posX, new_posY) not in visited):
                visited.add((new_posX, new_posY))

                if array[new_posX][new_posY] == 1:
                    defeatedEnemies += 1

                result = btEnemigos(N, M, enemies, array, new_posX, new_posY, moves - 1, visited, defeatedEnemies, directions)

                if result == "ATACA":
                    return "ATACA"

                visited.remove((new_posX, new_posY))
    return "CORRE"


N, M, enemigos = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input().strip().split())))

X, Y, D = map(int, input().split())
dirrecciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visitado = set()
enemigosDerrotados = 0

if array[X][Y] == 1:
    enemigosDerrotados += 1

visitado.add((X, Y))

# Llamada al resolver con los datos de entrada
resultado = btEnemigos(N, M, enemigos, array, X, Y, D, visitado, enemigosDerrotados, dirrecciones)
print(resultado)  # Esperado: ATACA o CORRE, dependiendo del caso
