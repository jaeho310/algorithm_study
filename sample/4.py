import heapq

def dijkstra(start, distance, graph, ans):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                ans[now] = 'YES'
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(g_nodes, g_edges, g_from, g_to, g_weight):
    # 다익스트라 알고리즘을 사용하므로 무한 정의
    INF = int(1e9)
    # 각 노드끼리의 최대거리 무한으로 초기화
    distance = [INF] * (g_nodes + 1)
    graph = [[] * (g_nodes + 1) for _ in range((g_nodes + 1))]

    for j in range(len(g_from)):
        a, b, c = g_from[j], g_to[j], g_weight[j]
        # c는 a->b까지의 비용
        graph[a].append((b, c))
    # 1번에서 시작해서 각 정점까지의 최단거리 계산
    ans = ['NO'] * g_edges
    dijkstra(g_from[0], distance, graph, ans)
    return ans

if __name__ == '__main__':
    print(solution(4, 5, [1,2,1,3,1], [2,4,3,4,4], [1,1,1,2,2]))