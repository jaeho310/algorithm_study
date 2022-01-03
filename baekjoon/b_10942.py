from collections import defaultdict

dp = defaultdict(list)

# def check(order, dp):
#     if arr[order[0]] != arr[order[1]]:
#         dp[order] = False
#     else:
#         dp[order] = True

def solution(arr, dp, start, end):
    break_time = (end - start) // 2
    cnt = 0
    while cnt < break_time:
        if end-cnt-1 not in dp[arr[start+cnt-1]]:
            return 0
        cnt += 1
    return 1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for el in arr:
        if el not in dp:
            res = [i for i, value in enumerate(arr) if value == el]
            dp[el] = res
    m = int(input())
    for _ in range(m):
        start, end = map(int, input().split())
        print(solution(arr, dp, start, end))
# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7

# 1
# 0
# 1
# 1