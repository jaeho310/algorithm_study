from collections import deque


def is_anagram(data1, data2):
    return ''.join(sorted(data1)) == ''.join(sorted(data2))

def solution(arr):
    temp = []
    arr = sorted(arr, key = lambda x: len(x))
    # for el in arr:
    #     temp.append(''.join(sorted(el)))
    ans = [arr.pop(0)]
    while arr:
        data = arr.pop(0)
        if not is_anagram(ans[-1], data):
            ans.append(data)
    return sorted(ans)


if __name__ == '__main__':
    print(solution(['code', 'aaagmnrs', 'anagrams', 'doce']))