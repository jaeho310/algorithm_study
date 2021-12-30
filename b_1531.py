from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    metrix = {}
    for i in range(0, 101):
        for j in range(0, 101):
            metrix[i,j] = 0
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                metrix[i,j] += 1

    ans = 0
    for k, v in metrix.items():
        if v > m:
            ans += 1
    print(ans)