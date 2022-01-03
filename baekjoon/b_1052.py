def solution1(N, K):
    def cheak(bottle_cnt):
        ans = 0
        while True:
            bottle_cnt, remain = divmod(bottle_cnt, 2)
            ans += remain
            num = bottle_cnt
            if num == 0:
                return ans

    bottle_cnt = N
    while True:
        if cheak(bottle_cnt) <= K:
            print(bottle_cnt - N)
            break
        bottle_cnt += 1


def solution2(N, K):
    purchased_water_bottle_cnt = 0

    while bin(N).count('1') > K:
        idx = bin(N)[::-1].index('1')
        purchased_water_bottle_cnt += 2 ** idx
        N += 2 ** idx

    print(purchased_water_bottle_cnt)

if __name__ == '__main__':
    N, K = map(int, input().split())
    solution2(N,K)

