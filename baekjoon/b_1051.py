metrix = []

def solution(m, n):
    global metrix
    top_left = 0
    top_right = 0
    bot_left = 0
    bot_right = 0
    ans = n
    cnt = 0
    while ans > 1:
        for i in range(0, n - ans + 1):
            for j in range(i, m - ans + 1):
                top_left = metrix[i][j]
                top_right = metrix[i][j + ans - 1]
                bot_left = metrix[i + ans - 1][j]
                bot_right = metrix[i + ans - 1][j + ans - 1]
                if top_left == top_right == bot_right == bot_left:
                    return ans * ans
        ans -= 1
    return 1

n, m = map(int, input().split())
for _ in range(n):
    metrix.append(input())
print(solution(m, n))

