from collections import defaultdict
import re

def get_str_list(str):
    start = 0
    end = 2
    temp_dict = defaultdict(int)
    # arr = []
    while True:
        if end > len(str):
            break
        split = str[start:end]
        if not split.isalpha():
            start += 1
            end += 1
            continue
        temp_dict[str[start:end]] += 1
        # arr.append(str[start:end])
        start += 1
        end += 1
    return temp_dict

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_dict = get_str_list(str1)
    str2_dict = get_str_list(str2)
    n12 = []
    u12 = []
    for k, v in str1_dict.items():
        if k in str2_dict:
            n12.append([k, min(v, str2_dict[k])])
            u12.append([k, max(v, str2_dict[k])])
        else:
            u12.append([k, str1_dict[k]])

    for k, v in str2_dict.items():
        if k not in str1_dict:
            u12.append([k, str2_dict[k]])
    # print('교집합: ', n12)
    # print('합집합: ', u12)
    ans1 = 0
    ans2 = 0
    for el in n12:
        ans1 += el[1]
    for el in u12:
        ans2 += el[1]
    if ans1 == 0 and ans2 == 0:
        return 65536
    ans = ans1 / ans2
    return int(ans * 65536)

if __name__ == '__main__':
    str1 = 'E=M*C^2'
    str2 = 'AAAA12'
    print(solution(str1, str2))