class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        i = 1
        j = 1
        # First element is always unique.
        # Increment j until you reach non-duplicate element and then store the value at nums[i]
        # This ensures that only the frist element of each "duplicate element subarray" is chosen in the main list
        # All other duplicates are simply overwritten safely.
        # Invariant: i <= j 
        while (j < n):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j +=1
        return i
