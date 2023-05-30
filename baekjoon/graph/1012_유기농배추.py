def solution(x, y):
    need_visited = [(x, y)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while need_visited:
        x, y = need_visited.pop()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    need_visited.append((nx, ny))
                    graph[nx][ny] = 0


def print_graph():
    for item in graph:
        print(item)


if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        m, n, k = map(int, input().split())
        graph = []
        ans = 0
        for i in range(m):
            graph.append([0] * n)
        for _ in range(k):
            a, b = map(int, input().split())
            graph[a][b] = 1
        # print_graph()
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    solution(i, j)
                    ans += 1
                    # print('+1')
                    # print_graph()
        print(ans)
        # print("answer = ", ans)