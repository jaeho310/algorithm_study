def solution(n, cnt):
    if len(n) == 1:
        print(cnt)
        if n == '3' or n == '6' or n == '9':
            print('YES')
        else:
            print('NO')
        return
    cnt += 1
    new_num = 0
    for i in n:
        new_num += int(i)
    solution(str(new_num), cnt)
    return


if __name__ == '__main__':
    n = input()
    solution(n, 0)
