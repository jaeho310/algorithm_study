#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxTrafficTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY start
#  2. INTEGER_ARRAY end
#

def getMaxTrafficTime(start, end):
    guest_list = []
    for i in range(len(start)):
        guest_list.append([start[i], end[i]])
    event_list = []
    for guest in guest_list:
        event_list.append([guest[0], 1])
        event_list.append([guest[1], -1])

    event_list = sorted(event_list, key=lambda x: (x[0], -x[1]))
    print(event_list)
    res = []
    max_cnt = 0
    current_cnt = 0
    for event in event_list:
        current_cnt += event[1]
        if current_cnt > max_cnt:
            max_cnt = current_cnt
            res.append([current_cnt, event[0]])
    sorted_res = sorted(res, key=lambda x: (-x[0], x[1]))
    print(sorted_res)
    return sorted_res[0][1]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    start_count = int(input().strip())

    start = []

    for _ in range(start_count):
        start_item = int(input().strip())
        start.append(start_item)

    end_count = int(input().strip())

    end = []

    for _ in range(end_count):
        end_item = int(input().strip())
        end.append(end_item)

    result = getMaxTrafficTime(start, end)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
