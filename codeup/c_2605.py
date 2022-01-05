from collections import deque

graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, color, graph):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if color == graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    if cnt >= 3:
        return 1
    return 0
if __name__ == '__main__':
    for _ in range(7):
        graph.append(list(map(int, input().split())))
    ans = 0
    for i in range(7):
        for j in range(7):
            if graph[i][j] == 0:
                continue
            ans += dfs(i, j, graph[i][j], graph)
    print(ans)
