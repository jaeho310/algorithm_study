# 1. Two Sum

class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)):
            if nums[i] in res:
                return [res.index(nums[i]), i]
            res.append(target - nums[i])