from sys import stdin
n, l = map(int, stdin.readline().split())

cnt = -1
while cnt<100:
    cnt += 1
    for i in range(1,n+1):
        arr = []
        for j in range(i, i + l + cnt):
            if(j > n):
                arr = []
                break
            arr.append(j)
        if sum(arr) == n:
            print(*arr)
            cnt = 100

if cnt == 100:
    print(-1)