# O(nlogn) time and O(n) space

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l: List[int] = nums.copy()
        l.sort()
        for i in range(len(l) - 1):
            arr = l[:i] + l[i+1:]
            if self.BSearch(arr, target - l[i]):
                return self.Find(nums, l[i], target - l[i])

    def Find(self, arr: List[int], x: int, y: int):
        i: int = -1
        j: int = -1
        for k in range(len(arr)):
            if (arr[k] == x and i == -1):
                i = k
            if (arr[k] == y and j == -1 and i != k):
                j = k
        return [i, j]

    def BSearch(self, arr: List[int], element: int) -> bool:
        n = len(arr)
        if n == 0:
            return False
        if n == 1:
            return arr[0] == element
        mid = len(arr)//2
        if element < arr[mid]:
            return self.BSearch(arr[:mid], element)
        elif element > arr[mid]:
            return self.BSearch(arr[mid + 1:], element)
        else:
            return True

# There are many other ways (e.g. two pointers) to do it in O(nlogn)
# But in fact, this can be solved in O(n) using hash maps 
# most algorithms can be optimised in some way using hash maps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = set()
        for i in nums:
            if target - i in d:
                x = nums.index(i)
                nums.remove(i)
                y = nums.index(target - i)
                if y >= x:
                    y += 1
                return [x, y]
            d.add(i)
            