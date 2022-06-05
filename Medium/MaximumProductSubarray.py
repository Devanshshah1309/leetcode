from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = max(nums[0], 0)
        n =  min(nums[0], 0)
        res = nums[0]

        for x in nums[1:]:
            a = 0
            b = 0
            if x >= 0:
                a = max(x, x*p)
                b =  x * n
            else:
                a = x * n
                b = min(x, x * p)
            res = max(res, a, b)
            a, p = p, a
            b, n = n, b
        return res

