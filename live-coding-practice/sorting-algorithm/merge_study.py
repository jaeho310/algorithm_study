def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    merged_arr = []
    left_idx = 0
    right_idx = 0
    while True:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

        if left_idx == len(left_arr):
            merged_arr.extend(right_arr[right_idx:])
            break
        if right_idx == len(right_arr):
            merged_arr.extend(left_arr[left_idx:])
            break
    return merged_arr

if __name__ == '__main__':
    arr = [3, 7, 1, 5, 4]
    print(merge_sort(arr))