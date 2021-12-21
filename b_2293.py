n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

# 1원부터 k원까지 만들수 있는 경우의 수 초기화
answer = [0] * (k + 1)

answer[0] = 1

for coin in coins:
    for j in range(coin, k + 1):
        # answer[j-coin]를 더해주는건 해당 값이 되기위해서 coin을 더하면되는데 coin을 뺐을때 나올수 있는 경우의수에다가 1 더해주면 되므로
        answer[j] += answer[j - coin]

print(answer[k])
