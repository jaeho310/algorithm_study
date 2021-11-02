n = int(input()) 
metrix = []
start = []
link = []
minAns = float('Inf')

for i in range(n):
    metrix.append(list(map(int, input().split())))
 
def dfs(index):
    global minAns
    if index == n // 2:
        startSum = 0
        linkSum = 0
        for i in range(0,n):
            if i not in start:
                link.append(i)

        for i in range(0, n // 2 - 1):
            for j in range(i+1, n // 2):
                startSum += metrix[start[i]][start[j]] + metrix[start[j]][start[i]]
                linkSum += metrix[link[i]][link[j]] + metrix[link[j]][link[i]]

        diff = abs(linkSum-startSum)
        if minAns > diff:
            minAns = diff
        link.clear()
        return
    
    for i in range(index,n+1):
        if i in start: continue
        if len(start)>0 and start[len(start)-1]> i : continue
        if i not in start:
            start.append(i)
            dfs(index +1)
            start.pop()
 
dfs(0)

print(minAns)