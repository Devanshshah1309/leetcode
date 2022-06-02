#O(n) time and O(n) space

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        print(c)
        for i in t:
            if i in c:
                c[i] -= 1
                if c[i] < 0:
                    return False
            else:
                return False
        for key in c:
            if c[key] != 0:
                return False
        return True