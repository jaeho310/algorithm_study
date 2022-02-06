from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    arr = []
    my_dict = defaultdict(int)
    ans_dict = defaultdict(int)
    answer = []
    for el in orders:
        for item in el:
            my_dict[item] += 1
    for k, v in my_dict.items():
        print(k, v)

if __name__ == '__main__':
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))