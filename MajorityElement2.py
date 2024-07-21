import math
import numpy as np
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret_arr = []
        x = math.floor(n/3)
        for i in range(n):
            if(nums.count(nums[i]) > x):
                ret_arr.append(nums[i])
        ret_set = set(ret_arr)
        ret_arr = list(ret_set)
        return ret_arr