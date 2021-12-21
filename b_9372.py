from sys import stdin
from collections import defaultdict
from collections import deque


def solution(graph, start):
    cnt = 0
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        current = queue.popleft()
        for node in graph[current]:
            if node not in visited:
                visited.append(node)
                queue.append(node)

    return len(visited)-1


if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split(' '))
        graph = defaultdict(list)
        # visit_check = [0] * n
        for _ in range(m):
            a, b = map(int, stdin.readline().strip().split())
            graph[a].append(b)
            graph[b].append(a)
        print(solution(graph, 1))


