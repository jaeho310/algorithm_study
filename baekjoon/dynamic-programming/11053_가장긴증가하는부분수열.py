if __name__ == '__main__':
    N = int(input())  # 수열의 길이
    arr = list(map(int, input().split()))  # 수열

    dp = [1] * N  # DP 배열 초기화

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    result = max(dp)  # 가장 긴 증가하는 부분 수열의 길이
    print(result)