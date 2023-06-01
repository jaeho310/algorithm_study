#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def print_matrix():
    for item in matrix:
        print(item)

def dfs(matrix, x, y, new_value):
    dx = [1, -1, 0, 0, 1, -1, -1]
    dy = [0, 0, 1, -1, -1, 1, -1]
    need_visited = [[x, y]]
    while need_visited:
        x, y = need_visited.pop()
        for i in range(7):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    need_visited.append([nx, ny])
                    matrix[nx][ny] = new_value
def connectedCell(matrix, n, m):
    new_value = 2
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(matrix, i, j, new_value)
                new_value += 1
    res = 0
    # print_matrix()
    for i in range(2, new_value):
        temp_cnt = 0
        for item in matrix:
            temp_cnt += item.count(i)
        res = max(res, temp_cnt)
    # res = 1
    # for el in matrix:
    #     res = max(res, max(el))
    if res == 0:
        return 1
    return res

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix, n, m)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
