# O(n) time, O(n) space

from typing import Dict, List

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        l: Dict[int, bool] = {} # can use set instead of dict for potential optimisation
        flag: bool = False
        for i in nums:
            if i in l:
                flag = True
            l[i] = True # arbitrary boolean value
        return flag