def is_under_prime(k):
    global primes
    d = 2
    cnt = 0
    # 그수 자체가 소수라면 cnt가 1이므로 x
    if k in primes:
        return False

    # 소수의 갯수를 구한다
    # 얘때문에 시간초과가 난다.
    while d <= k ** 2:
        if k % d == 0:
            cnt += 1
            k = k/d
        else:
            d += 1
    if cnt in primes:
        return True
    return False


if __name__ == '__main__':
    start, end = map(int, input().split())
    n = int(100000 ** 0.5)
    prime = [False] + [False] + [True] * 100000
    # 에라토스테네스의 체 방식으로 소수 리스트 정리
    for i in range(2, n + 1):
        if prime[i]:
            for k in range(i, 100001):
                if i * k > 100000:
                    break
                prime[i * k] = False
        if i * (i+1) > 100000:
            break
    # 소인수분해의 갯수를 dp로 한다.
    dp = [0] * (end + 1)
    for i in range(1, end+1):
        if prime[i]:
            dp[i] = 1
    for i in range(2, end+1):
        for j in range(2, end+1):
            if i * j > end:
                break
            if prime[j]:
                # 소수에다가 또 소수를 곱했으므로 그전의 소수갯수 + 1이 된다
                dp[i*j] = dp[i] + 1
    ans = 0
    for k in range(start, end+1):
        # if is_under_prime(k):
        #     ans += 1
        if prime[dp[k]]:
            ans += 1
    print(ans)

