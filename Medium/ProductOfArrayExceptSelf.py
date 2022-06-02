from functools import reduce
from collections import Counter
from typing import  List

# O(n) time, O(n) space
#
# definitely not the most elegant solution. I think you can use prefix and suffix multiplication
# something like this:
#
# output = [1] * len(nums)
# for i in range(1, len(nums)):
#     output[i] = nums[i - 1] * output[i - 1]
# for i in range(len(nums) - 2, -1, -1):
#     output[i] *= nums[i + 1]
#     nums[i] *= nums[i + 1]
# return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        c = Counter(nums)
        numOfZeroes = 0
        if 0 in c:
            numOfZeroes = c[0]
        if (numOfZeroes > 1):
            return [0 for _ in '.'*len(nums)]
        elif (numOfZeroes == 1):
            product = 1
            for n in nums:
                if n == 0:
                    continue
                product *= n
            output = []
            for i in nums:
                if i != 0:
                    output.append(0)
                else:
                    output.append(product)
            return output
        else:
            product = reduce(lambda x, y: x * y, nums)
            output = []
            for i in nums:
                output.append(product // i)
            return output