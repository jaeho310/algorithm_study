from collections import defaultdict

def solution():
    cnt = 0
    while True:
        cnt += 1
        n = int(input())
        check_dic = defaultdict(int)
        if n == 0:
            return
        stu_list = [''] * (n+1)
        for i in range(n):
            stu_list[i+1] = input()
        for i in range(2*n-1):
            a, b = input().split()
            check_dic[a] += 1
        for k, v in check_dic.items():
            if v != 2:
                print(cnt, stu_list[int(k)])


if __name__ == '__main__':
    solution()
