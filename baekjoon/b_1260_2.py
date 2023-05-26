from collections import defaultdict

def bfs_with_loop(graph, v):
    visited = []
    need_visited = [v]
    while need_visited:
        current = need_visited.pop(0)
        if current not in visited:
            visited.append(current)
            need_visited.extend(graph[current])
    return visited
def dfs_with_loop(graph, v):
    visited = []
    need_visited = [v]
    while need_visited:
        current = need_visited.pop()
        if current not in visited:
            visited.append(current)
            # 정점 번호가 작은걸 먼저 방문할꺼기에 뒤집에서 넣어준다.
            need_visited.extend((reversed(graph[current])))
    return visited

if __name__ == '__main__':
    matrix = defaultdict(list)
    n, m, v = map(int, input().split())
    for _ in range(m):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)
    for key in matrix:
        matrix[key].sort()
    print(dfs_with_loop(matrix, v))
    print(bfs_with_loop(matrix, v))
