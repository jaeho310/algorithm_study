arr = list()
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    for i in arr:
        print(i)
