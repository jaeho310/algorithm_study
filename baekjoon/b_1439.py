from collections import deque

def solution():
    queue = deque()
    n = input()
    for i in n:
        queue.append(i)

    ex_data = queue.popleft()
    cnt = 0
    while queue:
        data = queue.popleft()
        if ex_data != data:
            cnt += 1
        ex_data = data
    if cnt == 0:
        return 0
    elif cnt % 2 == 0:
        return cnt // 2
    else:
        return cnt // 2 + 1

if __name__ == '__main__':
    print(solution())