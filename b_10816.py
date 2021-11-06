n = int(input())
arr = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)


