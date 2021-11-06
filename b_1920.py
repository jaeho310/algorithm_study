def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return 1
    if len(data) == 1 and search != data[0]:
        return 0
    if len(data) == 0:
        return 0
    
    medium = len(data) // 2
    if search == data[medium]:
        return 1
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)


n = int(input())
target = list(map(int,input().split()))
m = int(input())
search = list(map(int,input().split()))

target.sort()
for i in search:
    print(binary_search(target, i))
