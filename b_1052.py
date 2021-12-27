N,K=map(int,input().split())

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
        print(bottle_cnt-N)
        break
    bottle_cnt += 1