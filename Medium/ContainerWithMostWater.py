# O(n) time and O(1) space
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1
        maxArea: int = 0
        # we decrement j when height[i] is greater than height[j] because incrementing i would not affect min(height[i], height[j]) but it would rather also decrease the width of the rectangle. In short, we remove the bottleneck that is weighing down the min(height[i], height[j]) by decreasing the width by 1 for a potential gain in min(height[i], height[j]) which would overcompensate and hence lead to larger area.
        while i < j:
            curr: int = (j - i)*min(height[i], height[j])
            if curr > maxArea:
                maxArea = curr
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
