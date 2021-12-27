# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9

dp = [0]*101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

def solution(n):
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))

