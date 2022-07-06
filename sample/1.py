from collections import defaultdict

def solution(arr):
    temp_dict = defaultdict(int)
    for el in arr:
        temp_dict[el] += 1
    res_arr = []
    for k, v in temp_dict.items():
        res_arr.append([k, v])
    return sorted(res_arr, key=lambda x: (-x[1], x[0]))


if __name__ == '__main__':
    print(solution([3, 3, 1, 2, 1]))