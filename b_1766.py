from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())

problem_list = [[] for i in range(n+1)]
# 기본적으로 자기한테 들어오는 간선이 없다고 가정하여 0으로 초기화
indegree = [0 for i in range(n+1)]

heap = []
result = []

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    problem_list[x].append(y)
    # 위상정렬을 위해 자기한테 들어오는 차수를 하나씩 올린다.
    indegree[y] += 1 

for i in range(1, n+1):
    # 차수가 0이라는건 뽑아도 된다는 뜻이므로 
    if indegree[i] == 0:
        # 정점의 index를 heap queue에 넣어준다.
        heapq.heappush(heap,i)
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for j in problem_list[data]:
        indegree[j]-=1
        # 차수를 줄여서 0이라면(나한테 들어오는게 없다면)
        # 내가 힙에 들어간다.
        if indegree[j] == 0:
            heapq.heappush(heap,j)
print(*result)
