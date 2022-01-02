from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0
    while True:
        data = queue.popleft()
        queue.append(data)
        cnt += 1
