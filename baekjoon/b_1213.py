from collections import defaultdict

def solution(s):
    alpha_dict = dict()
    ans = [0] * len(s)
    for i in s:
        if i in alpha_dict:
            alpha_dict[i] += 1
        else:
            alpha_dict[i] = 1
    alpha_dict = dict(sorted(alpha_dict))
    print(alpha_dict.keys())



if __name__ == '__main__':
    s = input()
    solution(s)