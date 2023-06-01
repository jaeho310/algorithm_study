if __name__ == '__main__':
    n, k = map(int, input().split())
    coin_list = []
    for _ in range(n):
        coin_list.append(int(input()))
    coin_list.sort(reverse=True)
    ans = 0
    for coin in coin_list:
        temp_ans, remain = divmod(k, coin)
        ans += temp_ans
        if remain == 0:
            break
        k = remain
    print(ans)