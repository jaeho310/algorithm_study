def solution(target, max_depth, res, idx):
    global ans
    if sum(res) == s:
        ans += 1
    if len(res) >= max_depth:
        return
    for i in range(idx, max_depth):
        res.append(arr[i])
        solution(target, max_depth, res, i+1)
        res.pop()

def solution2(idx, sub_sum):
    global ans2
    if idx >= n:
        return
    sub_sum += arr[idx]
    if sub_sum == s:
        ans2 += 1
    solution2(idx + 1, sub_sum)
    solution2(idx + 1, sub_sum - arr[idx])

if __name__ == '__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    ans2 = 0
    solution(s, n, [], 0)
    # solution2(0, 0)
    print(ans)
    # print(ans2)