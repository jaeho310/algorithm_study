def get_zero(n):
    if zero_list[n] != -1:
        return zero_list[n]
    zero_list[n] = get_zero(n-1) + get_zero(n-2)
    return zero_list[n]
def get_one(n):
    if one_list[n] != -1:
        return one_list[n]
    one_list[n] = get_one(n-1) + get_one(n-2)
    return one_list[n]

if __name__ == '__main__':
    test_cast = int(input())
    zero_list = [-1 for _ in range(41)]
    zero_list[0] = 1
    zero_list[1] = 0
    one_list = [-1 for _ in range(41)]
    one_list[0] = 0
    one_list[1] = 1
    for _ in range(test_cast):
        n = int(input())
        print(get_zero(n), end=' ')
        print(get_one(n))
