def solution(price, money, count):
    total_price = 0
    for i in range(count + 1):
        total_price += i * price
    if money >= total_price:
        return 0
    return abs(money-total_price)

if __name__ == '__main__':
    print(solution(3, 20, 4))