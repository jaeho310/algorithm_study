def solution(nums):
    half = len(nums) / 2
    nums = set(nums)
    return min(half, len(nums))

if __name__ == '__main__':
    print(solution([3,3,3,2,2,2]))