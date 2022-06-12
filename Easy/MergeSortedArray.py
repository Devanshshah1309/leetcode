from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        copyOfNums1 = nums1[:m].copy()
        i = 0
        j = 0
        while i < m and j < n:
            if copyOfNums1[i] <= nums2[j]:
                nums1[i+j] = copyOfNums1[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        while i < m:
            nums1[i+j] = copyOfNums1[i]
            i += 1
        while j < n:
            nums1[i+j] = nums2[j]
            j += 1