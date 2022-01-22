import math


def binary_search(arr, people):
    pass


if __name__ == '__main__':
    n, people = map(int, input().split())
    arr = []
    for _ in range(n):
        x, y, person = map(int, input().split())
        arr.append([round(math.sqrt(x**2+y**2), 3), person])
    arr.sort()
    binary_search(arr, people)