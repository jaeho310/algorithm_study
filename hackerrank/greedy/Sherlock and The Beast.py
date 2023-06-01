#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # 3을 5개씩 채우면서 나머지가 3의배수가 되는지 확인
    for i in range(n+1):
        if 5 * i > n:
            print(-1)
            return
        if (n - (5 * i)) % 3 == 0:
            cnt_3 = i * 5
            cnt_5 = n - cnt_3
            print(str('5' * cnt_5 + '3' * cnt_3))
            return


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

# 조건 1 3이나 5로 이루어진다
# 조건 2 3의 갯수는 5로 나누어진다
# 조건 3 5의 갯수는 3으로 나누어진다
# 조건 4 그중에 가장 커야된다
