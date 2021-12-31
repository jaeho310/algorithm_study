from collections import deque
queue = deque()
answer = list()

if __name__ == '__main__':
    n, k = map(int, input().split())
    for i in range(1, n+1):
        queue.append(i)

    while queue:
        for _ in range(k-1):
            data = queue.popleft()
            queue.append(data)
        answer.append(str(queue.popleft()))
    string_answer = "<"
    string_answer += ", ".join(answer)
    string_answer += ">"
    print(string_answer)
