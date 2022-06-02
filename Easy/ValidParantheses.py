#O(n) space and O(n) time

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        for i in s:
            if i in open:
                stack.append(i)
            elif i in close:
                if len(stack) == 0:
                    return False
                if open.index(stack[-1]) != close.index(i):
                    return False
                stack.pop()
        return len(stack) == 0