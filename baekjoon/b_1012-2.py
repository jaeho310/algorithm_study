def dfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                dfs(nx, ny)

if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        t = int(input())
        m, n, k = map(int, input().split())
        global matrix
        matrix = [[0] * m for _ in range(n)]
        answer = 0
        for i in range(k):
            a, b = map(int, input().split())
            matrix[a][b] = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dfs(i, j)
                    answer += 1

