def dfs(depth, idx, res):
    if depth == 6:
        print(*res)
        return

    for i in range(idx, total_cnt):
        res.append(array[i])
        dfs(depth + 1, i + 1, res)
        res.pop()

if __name__ == '__main__':
    while True:
        inputs = list(map(int, input().split()))
        total_cnt = inputs[0]
        array = inputs[1:]
        if total_cnt == 0:
            exit()
        dfs(0, 0, [])
        print()