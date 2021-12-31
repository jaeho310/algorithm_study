if __name__ == '__main__':
    arr = []
    n = input()
    for i in n:
        arr.append(i)
    arr.sort(reverse=True)
    print(int(''.join(arr)))
