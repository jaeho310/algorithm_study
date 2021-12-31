if __name__ == '__main__':
    n = int(input())
    memory = list(map(int, input().split()))
    m = int(input())
    question = list(map(int, input().split()))
    for q in question:
        if q in memory:
            print(1)
        else:
            print(0)
