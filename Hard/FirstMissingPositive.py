class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # just perform swaps to try and ensure that nums[i - 1] = i and then return the first index that does not match
        # for any number < 0 or > len(nums), we don't care since it definitely cannot be the smallest positive missing number
        # something like cuckoo hashing --> swap around till everything is as correctly positioned as possible
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # cannot directly swap due to nested evaluation of nums[i] which is evaluated after LHS? --> python bug maybe
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                return i + 1 
        return len(nums) + 1