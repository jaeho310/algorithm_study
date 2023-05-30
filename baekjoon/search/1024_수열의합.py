
if __name__ == '__main__':
    # 길이가 적어도 l인
    n, l = map(int, input().split())
    # 길이가 l보다 큰거로 구해지면 답
    # brute force
    condition = True
    while condition:
        res = []
        for i in range(1, n + 1):
            # 구간 합
            res_sum = 0
            for j in range(i, i + l):
                res_sum += j
            if res_sum == n:
                for j in range(i, i + l):
                    print(j, end=' ')
                exit()
            if res_sum > n:
                l += 1
                break
    print(-1)