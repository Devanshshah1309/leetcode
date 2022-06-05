from typing import List

# o(n^2) but somehow this works? (uses two pointer approach)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            target = 0 - num
            temp = []
            while l < r:
                sum = nums[l] + nums[r]
                if l == i or sum < target:
                    l += 1
                elif r == i or sum > target:
                    r -= 1
                else:
                    temp = [num, nums[l], nums[r]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                    l += 1
                    r -= 1
        return result