from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

b.sort()
a = sorted(a, reverse=True)

res = 0
for i in range(n):
    res += a[i] * b[i]
print(res)