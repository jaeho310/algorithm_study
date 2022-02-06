def solution(s):
    split = s.split('},{')
    ans = []
    temp = []
    for el in split:
        replaced = el.replace('{', '').replace('\'', '').replace('}', '')
        replaced_split = replaced.split(',')
        temp.append(replaced_split)
    arr = sorted(temp, key=lambda x: len(x))
    for el in arr:
        for item in el:
            if item not in ans:
                ans.append(item)
    return list(map(int, ans))

if __name__ == '__main__':
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))