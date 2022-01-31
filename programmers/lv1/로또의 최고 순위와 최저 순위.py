def solution(lottos, win_nums):
    zeros = 0
    cnt = 0
    rank_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5
        # 그외 6
    }
    for el in lottos:
        if el == 0:
            zeros += 1
            continue
        if el in win_nums:
            cnt += 1
    best = 6
    worst = 6
    if zeros + cnt in rank_dict.keys():
        best = rank_dict[zeros + cnt]
    if cnt in rank_dict.keys():
        worst = rank_dict[cnt]
    return [best, worst]

if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))