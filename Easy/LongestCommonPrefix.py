from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1