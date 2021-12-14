n, m = map(int,input().split())

whiteList = []
blackList = []

for i in range(1,8):
    if i % 2:
        whiteList.append('W')
        whiteList.append('B')
    else:
        blackList.append('B')
        blackList.append('W')
whiteList = ''.join(whiteList)
blackList = ''.join(blackList)

arr = []
answer = []
for _ in range(n):
    arr.append(input())

for i in arr:

