from sys import stdin
from math import ceil

def solution(n, a, b, answer):
    if a % 2 == 1 and a + 1 == b:
        return answer
    answer = solution(n // 2, ceil(a / 2), ceil(b / 2), answer + 1)
    return answer


if __name__ == '__main__':
    n, k, l = map(int, stdin.readline().split(' '))
    print(solution(n, min(k, l), max(k, l), 1))
