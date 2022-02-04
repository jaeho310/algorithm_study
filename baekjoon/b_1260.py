from collections import defaultdict

def bfs_with_loop(graph, v):
    visited = []
    need_visited = [v]
    while need_visited:
        current = need_visited.pop(0)
        if current not in visited:
            visited.append(current)
            need_visited.extend(graph[current])
    print(visited)


def dfs_with_loop(graph, v):
    visited = []
    need_visited = [v]
    while need_visited:
        current = need_visited.pop()
        if current not in visited:
            visited.append(current)
            need_visited.extend(reversed(graph[current]))
    print(visited)

def dfs_with_recur(graph, v, visited):
    currents = graph[v]
    for current in currents:
        if current not in visited:
            visited.append(current)
            return dfs_with_recur(graph, current, visited)
    return visited
    # print(visited)

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for key in graph:
        graph[key].sort()
    bfs_with_loop(graph, v)
    dfs_with_loop(graph, v)
    print(dfs_with_recur(graph,v,[v]))

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1