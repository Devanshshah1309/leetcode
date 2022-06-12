from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low= 0
        high = len(nums)
        while low < high:
            mid = (low + high)//2
            if low == mid:
                if target > nums[mid]:
                    return low + 1
                elif target <= nums[mid]:
                    return low
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid
            else:
                high = mid
