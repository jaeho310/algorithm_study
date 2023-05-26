import sys

# 파이썬 재귀 depth는 기본이 1000
# 스택에 그이상 쌓이도록하기위해 사용
sys.setrecursionlimit(10000)

case = int(input())

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

for i in range(case):
    m, n, k = map(int, input().split())

    # matrix 생성
    matrix = [[0] * m for _ in range(n)]
    answer = 0

    # 배추심기
    for i in range(k):
        a, b = map(int,input().split())
        matrix[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(i,j)
                answer += 1
    print(answer)
