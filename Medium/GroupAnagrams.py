from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            c = str(sorted(s))
            if c in d:
                d[c].append(s)
            else:
                d[c] = [s]
        return list(d.values())