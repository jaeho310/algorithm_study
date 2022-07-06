def solution(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    # 선택정렬 구현
    arr = [4,5,8,1,6]