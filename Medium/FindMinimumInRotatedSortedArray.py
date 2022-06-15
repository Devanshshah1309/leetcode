from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            # invariant: the minimum is always between start and end (incl.)
            # draw a graph to see the possible cases (only 2)
            mid = start + (end - start)//2
            if mid > start and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif mid < end and nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid] <= nums[start]:
                end = mid - 1
            else:
                start = mid + 1
        return nums[0] # no rotation performed so there is no "peak", where peak -> local minimum (both sides must be greater)
