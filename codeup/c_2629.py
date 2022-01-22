import math

def get_value(mid, arr):
    temp = 0
    distance = arr[mid][0]
    for el in arr:
        if el[0] <= distance:
            temp += p
            temp += el[1]
    return temp

def binary_search(arr):
    length = len(arr)
    start = 0
    end = length-1
    while start <= end:
        mid = start + end // 2
        value = get_value(mid, arr)
        if value > 1000000:
            end = mid - 1
        else:
            start = mid + 1
    return arr[end][0]


if __name__ == '__main__':
    n, p = map(int, input().split())
    arr = []
    for _ in range(n):
        x, y, person = map(int, input().split())
        arr.append([round(math.sqrt(x**2+y**2), 3), person])
    arr.sort()
    print(binary_search(arr))