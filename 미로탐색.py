def bfs(metrix):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    need_visit = []
    need_visit.append([0,0])
    visited = []    
    while need_visit:
        x, y = need_visit.pop(0)

        if [x, y] == [n-1, m-1]:
            print(metrix[x][y])

        if [x, y] not in visited:
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if (0 <= nx < n) and (0 <= ny < m):
                    if metrix[nx][ny] == 1:
                        need_visit.append([nx, ny])
                        metrix[nx][ny] = metrix[x][y] + 1
    
n, m = map(int, input().split())
metrix = []
for i in range(n):
    val = input()
    metrix.append([int(val[i]) for i in range(m)])

bfs(metrix)

    



