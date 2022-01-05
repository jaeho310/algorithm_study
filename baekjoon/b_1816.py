import sys


def solution(k):
    d = 2
    while d <= k ** 2:
        if d > 1000000:
            return 'YES'
        if k % d == 0:
            return 'NO'
        d += 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        k = int(sys.stdin.readline())
        print(solution(k))
