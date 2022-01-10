if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    while arr:
        pop = arr.pop()
        print(pop, end=' ')