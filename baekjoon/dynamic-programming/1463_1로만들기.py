def count_operations(n):
    # 결과를 저장할 리스트 초기화
    dp = [0] * (n + 1)

    # 1부터 n까지의 숫자에 대해 최소 실행 횟수 계산
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1  # n-1을 수행하는 경우

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누는 경우

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누는 경우

    return dp[n]

    return result
if __name__ == '__main__':
    n = int(input())
    # memo = [0] * (n + 1)
    memo = {}
    # for i in range(1, n + 1):
    #     memo[i] =
    print(count_operations(n))