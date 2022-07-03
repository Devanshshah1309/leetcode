class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find(val: int, l: list[int]) -> bool: # returns true iff val exists in l
            n = len(l)
            if n == 0: return False
            if n == 1: return val == l[0]
            mid = n//2
            if val < l[mid]:
                return find(val, l[:mid])
            elif val > l[mid]:
                return find(val, l[mid+1:])
            else:
                return True
        # Only called if val exists in l
        def findFirst(val: int, l: list[int]) -> int:
            n = len(l)
            if n == 0: return -1
            if n == 1: return 0
            i = 0
            j = len(l) - 1
            while i <= j:
                print(i, j)
                mid = i + (j-i)//2
                if (j - i) <= 1:
                    if l[i] == val:
                        return i
                    return j
                if val <= l[mid]:
                    j = mid
                else:
                    i = mid + 1
        # Only called if val exists in l
        def findLast(val: int, l: list[int]):            
            n = len(l)
            if n == 0: return -1
            if n == 1: return 0
            i = 0
            j = len(l) - 1
            while i <= j:
                mid = i + (j-i)//2
                if (j - i) <= 1:
                    if l[j] == val:
                        return j
                    return i
                if val < l[mid]:
                    j = mid - 1
                else:
                    i = mid
        
        if find(target, nums):
            return [findFirst(target, nums), findLast(target, nums)]
        return [-1, -1]