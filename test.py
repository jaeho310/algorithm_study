import heapq

if __name__ == '__main__':
    nums = [4, 1, 7, 3, 8, 5]
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
    while heap:
        print(heapq.heappop(heap))