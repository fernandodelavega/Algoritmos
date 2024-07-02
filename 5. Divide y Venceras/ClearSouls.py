def binary_search(levels, query, low, high):

    while low <= high:
        mid = (low + high) // 2
        if levels[mid] <= query:
            if mid == high or levels[mid + 1] > query:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


n = int(input())
heights = list(map(int, input().split()))

# Calcular sumas acumulativas de heights
cumulative_sums = [0] * n
cumulative_sums[0] = heights[0]
for i in range(1, n):
    cumulative_sums[i] = cumulative_sums[i - 1] + heights[i]
m = int(input())
sol = []
for _ in range(m):
    lvl = int(input())
    x = binary_search(heights, lvl, 0, n - 1)
    sol.append(x)

for i in sol:
    if i == -1:
        print("0 0")
    else:
        total_sum = cumulative_sums[i]
        print(f"{i + 1} {total_sum}")

