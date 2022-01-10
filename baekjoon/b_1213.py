from collections import defaultdict

def solution(s):
    dict = defaultdict(int)
    ans = [0] * len(s)
    for i in s:
        dict[i] += 1
    dict = sorted(dict)
    for i in range(len(s)//2):
        ans[i] = dict
    for k, v
    print(dict)


if __name__ == '__main__':
    s = input()
    solution(s)