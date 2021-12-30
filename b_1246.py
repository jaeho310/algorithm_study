from collections import deque
price_list = []
answer_list = []

def check(i, price_list, answer_list):
    cnt = 0
    for price in price_list:
        if i <= price <= i * 2:
            cnt += 1
            if cnt > n:
                return
    answer_list.append([i, cnt*i])

def solution(n, m, price_list, answer_list):
    for i in range(1, max(price_list)+1):
        check(i, price_list, answer_list)
    answer = max(answer_list, key=lambda x: x[1])
    for a in answer:
        print(a, end=' ')

def solution2():
    n, m = map(int, input().split())
    price_list = []
    for i in range(m):
        price_list.append(int(input()))
    price_list.sort()
    price, ans = 0, 0
    for i in range(m):
        mymax = min(m - i, n)
        if ans < price_list[i] * mymax:
            price = price_list[i]
            ans = price_list[i] * mymax
    print(price, ans)

if __name__ == '__main__':
    # n, m = map(int,input().split())
    # for _ in range(m):
    #     price_list.append(int(input()))
    # solution(n,m, price_list, answer_list)
    solution2()