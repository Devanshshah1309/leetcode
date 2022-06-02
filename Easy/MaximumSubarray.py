from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window technique?
        maximum = nums[0]
        current = 0
        for i in nums:
            current += i
            if current > maximum:
                maximum = current
            if current < 0:
                current = 0
        return maximum