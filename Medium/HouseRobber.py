from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        # dp[i] = max possible sum when nums[i] MUST be included
        dp = [None for _ in '.'*len(nums)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = dp[0] + nums[2]
        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        return max(dp[len(nums) - 1], dp[len(nums) - 2], dp[len(nums) - 3])