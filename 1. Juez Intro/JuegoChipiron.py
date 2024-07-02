n, b, a = map(str, input().strip().split())

int_n = int(n)

for i in range (1,int_n + 1):
    print(a*(int_n-i)+b*i)
