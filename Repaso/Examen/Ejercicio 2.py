def binarySearch(l, n):
    start = 0
    end = len(l)
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == n:
            return mid + 1
        if l[mid] < n:
            if mid == end or l[mid + 1] > n:
                return mid + 1
            else:
                start = mid + 1
        else:
            end = mid - 1

    return -1


lMc = list(map(int, input().strip().split()))
lFr = list(map(int, input().strip().split()))

gMc, gFr = map(int, input().strip().split())

cMc = binarySearch(lMc, gMc)
cFr = binarySearch(lFr, gFr)

print('{0} {1}'.format(cMc, cFr))
if cMc < cFr:
    print("FRANCESCO")
elif cMc > cFr:
    print("MCQUEEN")
else:
    print("EMPATE")
