from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    if maps[n - 2][m - 1] == 0 and maps[n - 1][m - 2] == 0:
        return -1

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    table = [[-1] * m for _ in range(n)]
    table[0][0] = 1

    q = deque()
    q.append([0, 0])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + directions[i][0]
            nx = x + directions[i][1]
            if nx >= 0 and nx <= (m - 1) and ny >= 0 and ny <= (n - 1):
                if maps[ny][nx] == 1 and table[ny][nx] == -1:
                    table[ny][nx] = table[y][x] + 1
                    q.append([ny, nx])

    return table[n - 1][m - 1]