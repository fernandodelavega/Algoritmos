def binarySearch(data, start, end, search):
    # caso base:
    if start > end:
        return -1
    # caso recurrente:
    else:
        mid = (start + end)//2
        if search == data[mid]:
            return mid
        elif search > data[mid]:
            res = binarySearch(data, mid + 1, end, search)
            if res == -1:
                return mid
            return res
        else:
            res = binarySearch(data, start, mid - 1, search)
            if res == -1:
                return mid
            return res


n = int(input())

players = []
for _ in range(n):
    players.extend(list(map(int, input().strip().split())))

dead = list(map(int, input().strip().split()))
deadList = players[:]

for d in dead:
    id = binarySearch(players, 0, len(players) - 1, d)
    data = players[id]
    while d > data:
        id += 1
        data = players[id]
    auxData = deadList[id]
    while auxData == -1 and id < n * n - 1:
        id += 1
        auxData = deadList[id]
    deadList[id] = -1

for i in range(n):
    for j in range(n):
        if deadList[i*n + j] == -1:
            print('X', end='')
        else:
            print(deadList[i*n + j], end='')
        if j != n - 1:
            print(' ', end='')
    if i != n - 1:
        print('')




