def getTotalTree(cut):
    totalTree = 0
    for treeHeight in treeHeightList:
        if treeHeight > cut:
            totalTree += treeHeight - cut
    return totalTree


def solution(target):
    left, right = 0, max(treeHeightList)
    while left <= right:
        mid = (left + right) // 2
        totalTree = getTotalTree(mid)
        # 너무 많이 짤랐다면 높이를 높혀 더 짜르자
        if totalTree >= target:
            left = mid + 1
        # 너무 적게 짤랐다면 높이를 낮춰서 더 짜르자
        else:
            right = mid - 1
    return right



if __name__ == '__main__':
    n, m = map(int,input().split())
    global treeHeightList 
    treeHeightList = list(map(int,input().split()))
    print(solution(m))
