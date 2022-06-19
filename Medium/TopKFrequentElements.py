# be sure to know libraries like heappq and the useful methods they offer
# no need to reinvent the wheel!!!
# you can also use sorted() and specify the comparison operator
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # create a list of unique elements only
        # define a sort key
        def fun(i):
            return c[i] # sort based on frequency
        uniques = list(c.keys()) # since keys are unique in a dictionary
        return heapq.nlargest(k, uniques, fun)

# an even shorter solution is using most_common as follows:
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return map(lambda x: x[0], map(list, Counter(nums).most_common(k)))
