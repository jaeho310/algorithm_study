def solution(arr):
    for i in range(len(arr), 0, -1):
        for j in range(i):
            if j == len(arr)-1:
                continue
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    arr = [6, 2, 7, 1]
    print(solution(arr))