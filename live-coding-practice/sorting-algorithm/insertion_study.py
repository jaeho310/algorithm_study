def solution(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr

if __name__ == '__main__':
    arr = [5, 2, 3, 1, 7]
    print(solution(arr))