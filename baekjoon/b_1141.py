if __name__ == '__main__':
    n = int(input())
    queue = list()
    for _ in range(n):
        queue.append(input())
    queue.sort(key=lambda x: len(x))
    answer = 0
    last_data = queue[-1]
    while queue:
        cnt = 0
        data = queue.pop(0)
        for i in queue:
            is_contain = True
            for j in range(len(data)):
                if data[j] != i[j]:
                    is_contain = False
                    break
            if not is_contain:
                cnt += 1
        answer = max(answer, cnt+1)
        if data == last_data:
            break
    print(answer)