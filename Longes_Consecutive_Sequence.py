class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet: 
                current = num
                currentLength = 1
                while current + 1 in numSet:
                    current += 1
                    currentLength += 1
                longest = max(longest, currentLength)
        return longest