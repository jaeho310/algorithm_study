import itertools
import math


def is_prime(num):
    temp = 2
    while temp <= math.sqrt(num):
        if num % temp == 0:
            return False
        temp += 1
    return True

def solution(nums):
    answer = 0
    arr = list(itertools.combinations(nums, 3))
    for el in arr:
        if is_prime(sum(el)):
            print(el)
            answer += 1
    return answer
if __name__ == '__main__':
    print(solution([1,2,7,6,4]))