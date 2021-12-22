from sys import stdin

def solution(n, k, cnt, water):
    if n % 2 != 0:
        cnt += water
        n += 1
    # next_bottle = n//2
    # if next_bottle % 2 != 0:
        # cnt += rec_cnt * 2
        # next_bottle += 1
    if n <= k:
        return cnt
    cnt = solution(next_bottle, k, cnt, rec_cnt+1)
    return cnt

if __name__ == '__main__':
    n, k = map(int, stdin.readline().split())
    print(solution(n, k, 0, 1))