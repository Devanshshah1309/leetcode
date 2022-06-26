from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        swaps = 0
        while i <= j:
            if nums[i] == val: # swap all elements to be removed to the end of the list
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                swaps += 1
            else:
                i += 1
            print(nums)
        return len(nums) - swaps
