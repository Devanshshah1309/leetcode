from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1
        maxArea: int = 0
        while i < j:
            curr: int = (j - i)*min(height[i], height[j])
            if curr > maxArea:
                maxArea = curr
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea