from sys import stdin

l = int(stdin.readline())
s = list(map(int, stdin.readline().split()))
n = int(stdin.readline()) 

start = 0
end = 0
answer = []
if n in s:
    print(0)
else:
    for i in range(len(s)):
        if s[i] < n and n < s[i+1]:
            start  = s[i]
            end = s[i+1]
            break

# # if n - start != 1 and end - n != 1:
# for i in range(start+1, end):
#     if i > n :
#         break
#     for j in range(i+1, end):
#         answer.append([i,j])

print(end-start+(end-n)*(n-start))
