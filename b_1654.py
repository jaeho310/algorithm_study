import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수
    if lines >= N: # 원하는 랜선보다 많이짤린경우 랜선수를 줄이면서 간다.
        start = mid + 1
    else:
        end = mid - 1
print(end)