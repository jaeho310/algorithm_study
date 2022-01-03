import math

def solution(ex_win_rate):
    start = 0
    end = 1000000000
    while start <= end:
        mid = (start + end) // 2
        new_win_rate = math.floor((y+mid)/(x+mid) * 100)
        if ex_win_rate < new_win_rate:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
x, y = map(int, input().split())
if x == y:
    print(-1)
else:
    current_win_rate = math.floor(y/x * 100)
    print(solution(current_win_rate))