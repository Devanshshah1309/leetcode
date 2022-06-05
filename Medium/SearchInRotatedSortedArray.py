from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivotIndex(nums)
        if pivot == -1:
            return self.searchTarget(nums, target, 0, len(nums)-1)
        
        if target == nums[pivot]:
            return pivot
        elif target < nums[0]:
            return self.searchTarget(nums, target, pivot+1, len(nums)-1)
        else:
            return self.searchTarget(nums, target, 0, pivot)

    def pivotIndex(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start + (end-start)//2 
            if mid>start and nums[mid]<nums[mid-1]:
                return mid-1
            if mid<end and nums[mid]>nums[mid+1]:
                return mid
            if nums[start] >= nums[mid]:
                end = mid-1
            else:
                start = mid+1
        return -1
        
    def searchTarget(self, nums: List[int], target: int, start, end) -> int:
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid +1
            else:
                return mid
        return -1
            
