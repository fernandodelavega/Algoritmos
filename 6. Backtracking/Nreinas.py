def nReinas(tablero, columna, n):
    if columna >= n:
        return 1
    soluciones = 0
    for fila in range(n):
        if esSeguro(tablero, fila, columna, n):
            tablero[fila][columna] = 1
            soluciones += nReinas(tablero, columna + 1, n)

    return soluciones

def esSeguro(tablero, fila, columna, n):
    for i in range(columna):
        if tablero[fila][i] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, n, 1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False




    return True



n = int(input().strip())
tablero = [[0]*n for _ in range(n)]

nsol = nReinas(tablero, 0, n)
print(nsol)