def solution(depth, res):
    if depth == m:
        print(*res)
        return
    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            solution(depth + 1, res)
            res.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    solution(0, [])