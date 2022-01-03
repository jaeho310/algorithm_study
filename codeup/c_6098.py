def solution(metrix, a, b):
    metrix[a][b] = 9
    if metrix[a][b+1] == 2:
        metrix[a][b+1] = 9
        return
    if metrix[a][b+1] == 0:
        solution(metrix, a, b+1)
    elif metrix[a][b+1] == 1 and metrix[a+1][b] == 0:
        solution(metrix, a+1, b)
    elif metrix[a + 1][b] == 2:
        metrix[a + 1][b] = 9
        return
    else:
        return


if __name__ == '__main__':
    metrix = []
    for _ in range(10):
        metrix.append(list(map(int, input().split())))
    solution(metrix, 1, 1)
    for m in metrix:
        print(" ".join(map(str, m)))
