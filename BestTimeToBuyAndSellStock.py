import numpy as np
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) != 1):
            max_diff = prices[1] - prices[0]
            min_element = prices[0]
            for i in range(1,len(prices)):
                if ((prices[i] - min_element)>max_diff):
                    max_diff = prices[i] - min_element
                if (prices[i] < min_element):
                    min_element = prices[i]
            if (max_diff < 0):
                return 0
            else:
                return max_diff
        else:
            return 0