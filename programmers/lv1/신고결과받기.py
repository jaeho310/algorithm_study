from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(list)
    threshold_dict = defaultdict(int)
    for el in report:
        reporting, reported = el.split()
        if reported not in report_dict[reporting]:
            report_dict[reporting].append(reported)
            threshold_dict[reported] += 1
    for el in id_list:
        temp = 0
        for item in report_dict[el]:
            if threshold_dict[item] >= k:
                temp += 1
        answer.append(temp)
    return answer

if __name__ == '__main__':
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    # report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    # k = 2
    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))