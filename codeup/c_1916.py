import sys


def fibo(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

def solution(n):
    print(fibo(n)%10009)


if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
        sys.exit()
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    solution(n)