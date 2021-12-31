from collections import defaultdict

c, n = map(int,input().split())
arr = []

for _ in range(n):
    cost, value = map(int,input().split())
    arr.append([cost, value, value / cost])

arr = sorted(arr, key= lambda x: x[2], reverse=True)
idx = 0
answer = 0
cnt = 0
while cnt < c:
    if arr[idx][1] > c:
        idx += 1
        continue
    answer += arr[idx][0]
    cnt += arr[idx][1]
print(answer)