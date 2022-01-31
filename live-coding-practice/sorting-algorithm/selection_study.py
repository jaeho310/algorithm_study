def solution(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr



if __name__ == '__main__':
    arr = [5,2,4,1,3,7]
    print(solution(arr))