def solution(graph, n, m):
    need_visited = [[0, 0]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    while need_visited:
        x, y = need_visited.pop(0)
        if [x, y] == [n-1, m-1]:
            return graph[x][y]
        if [x, y] not in visited:
            visited.append([x, y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1:
                        need_visited.append([nx, ny])
                        graph[nx][ny] = graph[x][y] + 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        sub = list(map(int, input()))
        graph.append(sub)
    for item in graph:
        print(item)
    print(solution(graph, n, m))