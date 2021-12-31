from collections import defaultdict

answer = defaultdict(list)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        length = len(s)
        if s not in answer[length]:
            answer[length].append(s)

    key_list = list(answer.keys())
    key_list.sort()
    for i in key_list:
        if len(answer[i]) != 1:
            answer[i].sort()
        for ans in answer[i]:
            print(ans)