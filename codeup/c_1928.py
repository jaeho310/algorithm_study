def solution(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 1:
        solution(3*n + 1)
    else:
        solution(n // 2)
    return


if __name__ == '__main__':
    n = int(input())
    solution(n)
