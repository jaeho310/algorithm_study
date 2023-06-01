if __name__ == '__main__':
    n = int(input())
    times = list(map(int, input().split()))
    times.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += (i+1) * times[i]
    print(ans)