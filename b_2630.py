from sys import stdin
def solution(metrix, start, end, white, blue):
    color = metrix[start][start]
    is_same = True
    for i in range(start, end):
        for j in range(i, end):
            if metrix[i][j] != color:
                is_same = False
                break
    if not is_same:
        w_cnt, b_cnt = solution(metrix, start, end//2, white, blue)
        white += w_cnt
        blue += b_cnt
        w_cnt, b_cnt = solution(metrix, end//2, end, white, blue)
        white += w_cnt
        blue += b_cnt

    if color == 0:
        white += 1
    elif color == 1:
        blue += 1
    return white, blue


            
            


n = int(stdin.readline())
metrix = []
for i in range(n):
    metrix.append(list(map(int,stdin.readline().split())))
print(solution(metrix, 0, n,  0, 0))

