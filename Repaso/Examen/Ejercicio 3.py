import copy
def isViable(x, y, r, tablero, fils, cols):
    n_cubiertos = 0
    tablero_aux = copy.deepcopy(tablero)

    for i1 in range(0, r + 1):
        if 0 <= y + i1 <= cols - 1:
            if tablero_aux [x][y + i1] == -1:
                break
            if tablero_aux [x][y + i1] == 0:
                n_cubiertos += 1
                tablero_aux[x][y + i1] = 2

    for i2 in range(0, -r-1, -1):
        if 0 <= y + i2 <= cols - 1:
            if tablero_aux [x][y + i2] == -1:
                break
            if tablero_aux [x][y + i2] == 0:
                n_cubiertos += 1
                tablero_aux[x][y + i2] = 2

    for j in range(0, r+1):
        if 0 <= x + j <= fils - 1:
            if tablero_aux [x + j][y] == -1:
                break
            if tablero_aux [x + j][y] == 0:
                n_cubiertos += 1
                tablero_aux[x + j][y] = 2
    for j2 in range(0, -r-1, -1):
        if 0 <= x + j2 <= fils - 1:
            if tablero_aux [x + j2][y] == -1:
                break
            if tablero_aux [x + j2][y] == 0:
                n_cubiertos += 1
                tablero_aux[x + j2][y] = 2
    return n_cubiertos, tablero_aux


def backtrack(fil, col, ran, arr, mur):
    cel_L = col * fil - mur
    arr_aux = copy.deepcopy(arr)

    for i in range(fil):
        Maxcubiertas = 0
        for j in range(col):
            if arr[i][j] != -1:
                maxC, aux = isViable(i, j, ran, arr_aux, fil, col)
                if maxC > Maxcubiertas:
                    Maxcubiertas = maxC
                    arr_aux2 = aux
        cel_L -= Maxcubiertas
        arr_aux = arr_aux2
    return cel_L, arr_aux


n, m, r = map(int, input().strip().split())
a = []
muros = 0
for i in range(n):
    a.append(list(map(int, input().strip().split())))
    for j in range(m):
        if a[i][j] == -1:
            muros += 1
sol, solT = backtrack(n, m, r, a, muros)

print(sol)


