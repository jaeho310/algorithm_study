def solution(n, k):
    print((n**k)%1000000007)
    # dp = [0] * (n + 1)
    # dp[1] = 1
    # for i in range(2, n+1):
    #     dp[i] = dp[i-1] + (2*i - 1)
    # print(dp[n])

if __name__ == '__main__':
    n, k = map(int,input().split())
    solution(n, k)