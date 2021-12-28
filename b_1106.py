if __name__ == '__main__':
    dp = [float('inf')] * 5000
    dp[0] = 0
    c, n = map(int,input().split())
    for _ in range(n):
        cost, customer_cnt = map(int, input().split())
        for i in range(0, 5000):
            if dp[i] == float('inf'):
                continue
            for j in range(1, 5000):
                if j*customer_cnt + i >= 5000:
                    break
                dp[i+customer_cnt*j] = min(dp[i+customer_cnt*j], dp[i]+cost*j)
    print(dp[c])

