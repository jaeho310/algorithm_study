from collections import defaultdict
from collections import deque

def search(tree, start, ans):
    queue = deque()
    queue.append([tree[start], start])
    while queue:
        data = queue.popleft()
        for el in data[0]:
            if el not in ans:
                ans[el] = data[1]
                queue.append([tree[el], el])
    return ans

if __name__ == '__main__':
    tree = defaultdict(list)
    n = int(input())
    for _ in range(n-1):
        a, b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    # tree = sorted(tree.items(), key=lambda x: x[0])
    # print(tree)
    ans = search(tree, 1, {})
    ans = sorted(ans.items(), key=lambda x:x[0])
    for i in range(1, n):
        print(ans[i][1])