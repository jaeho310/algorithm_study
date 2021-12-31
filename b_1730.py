def can_go(n, o):
    if o < 0 or n < o:
        return False
    return True

def solution(order, metrix, n):
    a, b = 0, 0
    for o in order:
        if o == 'D':
            if not can_go(n, a+1):
                continue
            if metrix[a][b] == '-':
                metrix[a][b] = '+'
            else:
                metrix[a][b] = '|'
            a += 1
        elif o == 'U':
            if not can_go(n, a-1):
                continue
            if metrix[a][b] == '-':
                metrix[a][b] = '+'
            else:
                metrix[a][b] = '|'
            a -= 1
        elif o == 'L':
            if not can_go(n, b-1):
                continue
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            else:
                metrix[a][b] = '-'
            b -= 1
        elif o == 'R':
            if not can_go(n, b+1):
                continue
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            else:
                metrix[a][b] = '-'
            b -= 1
    return metrix
if __name__ == '__main__':
    n = int(input())
    metrix = [['.']*n]*n
    order = input()
    print(solution(order, metrix, n))