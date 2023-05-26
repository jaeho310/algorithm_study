import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘려줍니다.

def dfs(graph, start, visited):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    count = 0

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1

    print(count)