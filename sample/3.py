def solution(s):
    stack = list(s)
    check = [0, 0]
    ans = []
    res = []
    while stack:
        if not res:
            data = stack.pop(0)
            res.append(data)
            if data == 1:
                check[1] += 1
            else:
                check[0] += 1
            continue
        data = stack.pop(0)
        if stack[-1] != data:
            res.append(data)
            if data == 1:
                check[1] += 1
            else:
                check[0] += 1
        if check[0] == check[1] and ''.join(res) not in ans:
            ans.append(res)


    pass

if __name__ == '__main__':
    print(solution('00110'))