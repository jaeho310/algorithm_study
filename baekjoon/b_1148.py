from collections import defaultdict

def solution(arr, order):
    word_dict = defaultdict(int)
    answer_dict = defaultdict(int)
    for el in order:
        word_dict[el] += 1
    for el in arr:
        temp_dict = defaultdict(int)
        is_available = True
        for val in el:
            temp_dict[val] += 1
            if temp_dict[val] > word_dict[val]:
                is_available = False
                break
        if is_available:
            for k, v in temp_dict.items():
                answer_dict[k] += 1
            # print(word_dict)
            # print(temp_dict)
    answer_dict = sorted(answer_dict.items(), key=lambda x: x[1])
    min_word = answer_dict[0][0]
    min_cnt = answer_dict[0][1]
    max_word = answer_dict[-1][0]
    max_cnt = answer_dict[-1][1]
    answer_dict = dict(answer_dict)
    print(answer_dict)
    for k, v in answer_dict.items():
        if v == min_cnt:
            min_word += k
            continue
        if v == max_cnt:
            max_word += k
    return min_word, min_cnt, max_word, max_cnt

def solution2(arr, order):
    word_dict = defaultdict(int)
    # cannot_dict는 해당단어가 가운데에 들어가면 만들수없는 단어의 갯수이다.
    answer_dict = defaultdict(int)
    can_dict = defaultdict(list)
    for el in order:
        word_dict[el] += 1
        for val in arr:
            if el in val:
                can_dict[el].append(val)
        # word_dict[el] += 1
    # for el in arr:
    #     for val in el:
    print(can_dict)
    for k, v in can_dict.items():
        temp_dict = defaultdict(int)
        is_available = True
        for val in v:
            temp_dict[val] += 1
            if temp_dict[val] > word_dict[val]:
                is_available = False
                break
        print(temp_dict)
        # if is_available:
        #     for key, vvalue in temp_dict.items():
        #         answer_dict[key] += 1


if __name__ == '__main__':
    arr = []
    while True:
        s = input()
        if s == '-':
            break
        arr.append(s)
    while True:
        s = input()
        if s == '#':
            break
        print(solution2(arr, s))
