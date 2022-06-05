from typing import List

# O(n^2logn) time and O(1) space - TLE
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if self.BSearch(-nums[x]-nums[y], nums[y + 1:]):
                    p = [nums[x], nums[y], -nums[x] - nums[y]]
                    if p not in ans:
                        ans.append(p)
                    
        
        return ans

    def BSearch(self, value: int, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == value
        else:
            mid = len(nums)//2
            if nums[mid] < value:
                return self.BSearch(value, nums[mid + 1 :])
            elif nums[mid] > value:
                return self.BSearch(value, nums[:mid])
            else:
                return True

    