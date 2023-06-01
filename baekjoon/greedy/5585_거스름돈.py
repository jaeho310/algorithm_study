def solution(n):
    res = 0
    for coin in coin_list:
        current_res, b = divmod(n, coin)
        if b == 0:
            break
        n = b
        res += current_res
    print(res)


if __name__ == '__main__':
    coin_list = [500, 100, 50, 10, 5, 1]
    n = int(input())
    solution(1000 - n)