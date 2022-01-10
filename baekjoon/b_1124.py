def is_under_prime(k):
    global primes
    d = 2
    cnt = 0
    if k in primes:
        return False
    while d <= k ** 2:
        if k % d == 0:
            cnt += 1
            k /= d
        else:
            d += 1
    if cnt in primes:
        return True
    return False


if __name__ == '__main__':
    n = 50
    a = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    start, end = map(int, input().split())
    ans = 0
    for k in range(start, end+1):
        if is_under_prime(k):
            ans += 1
    print(ans)

