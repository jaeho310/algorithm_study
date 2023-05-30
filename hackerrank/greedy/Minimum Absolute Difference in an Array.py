#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' funtion below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    min_value = 10 ** 5
    arr.sort()
    for index in range(0, len(arr) - 1):
        min_value = min(min_value, abs(arr[index] - arr[index + 1]))
    return min_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
