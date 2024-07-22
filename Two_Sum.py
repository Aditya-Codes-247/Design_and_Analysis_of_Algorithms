import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in arr:
                return [arr[c], i]
            arr[num] = i
        return []