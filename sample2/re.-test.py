import re
from collections import defaultdict

if __name__ == '__main__':
    arr = [1,2,3]
    arr2 = [3,4,5]
    res = []
    for i in range(len(arr)):
        res.append([arr[i], arr2[i]])
    print(res)