arr = []
if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(1, b+1):
        for _ in range(i):
            arr.append(i)
    print(sum(arr[a-1:b]))


