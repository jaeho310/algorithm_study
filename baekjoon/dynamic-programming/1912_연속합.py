if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]] * n
    for i in range(1, n):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    print(max(dp))
