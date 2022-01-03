N,K = map(int,input().split())

naegoo = list(map(int,input().split()))

robot=[0]*N

step=0
while(naegoo.count(0)<K):
    step+=1
    a=naegoo.pop()
    naegoo.insert(0,a)

    robot.pop()
    robot.insert(0,0)

    robot[N - 1] = 0

    for i in range(N-2,0,-1):
        if robot[i] and naegoo[i+1] and (not robot[i+1]):
            robot[i]=0
            robot[i+1]=1
            naegoo[i+1] = max(0,naegoo[i+1]-1)

    robot[N - 1] = 0

    if naegoo[0] and (not robot[0]):
        robot[0]=1
        naegoo[0] = max(0,naegoo[0]-1)

print(step)