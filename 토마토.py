import collections

metrix = []
need_visit = collections.deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int,input().split())

for i in range(m):
    row = list(map(int, input().split()))
    metrix.append(row)

# 익어있는 곳 찾기
for i,j in enumerate(metrix):
    if 1 in j:
        for a,b in enumerate(j):
            if b == 1:
                need_visit.append([i,a])

# bfs
while need_visit:
    x,y = need_visit.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and metrix[nx][ny] == 0:
            need_visit.append([nx,ny]) 
            metrix[nx][ny] = metrix[x][y] + 1


# 모든 토마토가 안익었는지 확인
flag = False
answer = -2


# 안익은게 남아있다는건 애초에 익은토마토가 없다는 뜻
for i in metrix:
    for j in i:
        if j == 0:
            flag = True
        answer = max(answer,j) # 최댓값 확인

if flag == True:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer-1)