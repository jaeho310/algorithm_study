def solution(a, b):
    max_val = max(a, b)
    min_val = min(a, b)
    cnt = 1
    answer = 0
    while True:
        temp = max_val * cnt
        if temp % min_val == 0:
            answer = temp
            break
        cnt += 1
    return answer

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(solution(a, b))