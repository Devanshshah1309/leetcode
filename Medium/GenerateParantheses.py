from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def sol(l, r, s):
            if l == 0 and r == 0:
                res.append(s)
                return 
            if l > 0:
                sol(l - 1, r + 1, s + "(")
            if r > 0:
                sol(l, r - 1, s + ")")
        sol(n, 0, "")
        return res
