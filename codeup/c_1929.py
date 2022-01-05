def solution(n):
    if n == 1:
        print(n)
        return
    if n % 2 == 1:
        solution(3 * n + 1)
    else:
        solution(n // 2)
    print(n)
if __name__ == '__main__':
    n = int(input())
    solution(n)