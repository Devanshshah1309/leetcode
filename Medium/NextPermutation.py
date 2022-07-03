from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Identify the last sorted consecutive elements. This leads to 3 cases:
        # If there is an inversion --> perform a swap and reverse the rest of the elements (key insight to solving this problem)
        # If there is no inversion at all --> array is reverse sorted. So, we just reverse it.
        pointer=0
        length=len(nums)
        if length<=2:
            return nums.reverse()
        pointer=length-2
        while(pointer>=0 and nums[pointer]>=nums[pointer+1]):
            pointer-=1
        if pointer==-1:
            return nums.reverse()
        for i in range(length-1,pointer,-1):
            if nums[pointer]<nums[i]:
                nums[pointer],nums[i]=nums[i],nums[pointer]
                break
    
        nums[pointer+1:]=nums[length-1:pointer:-1]
