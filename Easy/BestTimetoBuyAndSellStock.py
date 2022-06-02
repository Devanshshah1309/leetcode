# O(n) time and O(1) space

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff: int = 0 # stores the prefix maximum difference
        lowest: List[int] = prices[0] # stores the prefix maximum
        for i in prices:
            if (i - lowest) > maxDiff:
                maxDiff = i - lowest
            if i < lowest:
                lowest = i

        return maxDiff