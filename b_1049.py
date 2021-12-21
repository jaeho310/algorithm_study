from sys import stdin

n, m = map(int, stdin.readline().split())

answer = 0
package_price = []
price = []
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    package_price.append(a)
    price.append(b)

min_package_price = min(package_price)
min_prcie = min(price)

if min_prcie * 6 < min_package_price:
    print(answer)
else:
    package_cnt, remain_cnt = divmod(n, 6)
    answer += package_cnt * min_package_price

    if remain_cnt * min_prcie < min_package_price:
        answer += remain_cnt * min_prcie
    else:
        answer += min_package_price
    print(answer)