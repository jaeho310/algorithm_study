def solution(x):
    res = []
    while x:
        if x[:4] == 'XXXX':
            res.append('AAAA')
            x = x[4:]
        elif x[:2] == 'XX':
            res.append('BB')
            x = x[2:]
        elif x[0] == '.':
            res.append('.')
            x = x[1:]
        else:
            return -1
    return ''.join(res)


if __name__ == '__main__':
    x = input()
    print(solution(x))