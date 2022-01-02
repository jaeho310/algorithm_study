def can_go(n, o):
    if o < 0 or n-1 < o:
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
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '|'
            a += 1
            if metrix[a][b] == '-':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '|'
        elif o == 'U':
            if not can_go(n, a-1):
                continue
            if metrix[a][b] == '-':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '|'
            a -= 1
            if metrix[a][b] == '-':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '|'
        elif o == 'L':
            if not can_go(n, b-1):
                continue
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '-'
            b -= 1
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '-'
        elif o == 'R':
            if not can_go(n, b+1):
                continue
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '-'
            b += 1
            if metrix[a][b] == '|':
                metrix[a][b] = '+'
            elif metrix[a][b] == '+':
                pass
            else:
                metrix[a][b] = '-'
    for m in metrix:
        print(''.join(m))

metrix = []

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append('.')
        metrix.append(temp)
    order = input()
    solution(order, metrix, n)