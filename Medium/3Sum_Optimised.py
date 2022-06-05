from collections import Counter
from typing import List

# O(n^2) time and O(1) space - TLE
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        ans = []
        for x in nums:
            for y in nums:
                if -x-y in c:
                    if x == y and c[x] > 1:
                        if x == 0:
                            if c[x] > 2:
                                a = [0, 0, 0]
                                if a not in ans:
                                    ans.append(a)
                        else: # x != 0 and x == y 
                            a = [x, y, -x-y]
                            a.sort()
                            if a not in ans:
                                ans.append(a)
                    elif x == -x-y and x != y and c[x] > 1:
                        a = [x, y, -x-y]
                        a.sort()
                        if a not in ans:
                            ans.append(a)
                    elif y == -x-y and c[y] > 1 and x != y:
                        a = [x, y, -x-y]
                        a.sort()
                        if a not in ans:
                            ans.append(a)
                    elif x != y and x != -x-y and y != -x-y:
                        a = [x, y, -x-y]
                        a.sort()
                        if a not in ans:
                            ans.append(a)

        return ans