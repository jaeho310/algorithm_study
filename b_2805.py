n, m = map(int, input().split())
treeList = list(map(int,input().split()))

start, end = 1, max(treeList)
while start <= end:
    height = (start + end) // 2
    total = 0
    for i in treeList:
        if i >= height:
            total += i - height
    # 나무가 너무 많이 나왔다면
    if total >= m:
        start = height + 1
    # 적게 나왔다면
    else:
        end = height - 1
print(end)
