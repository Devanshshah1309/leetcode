from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry + digits[i] <= 9:
                digits[i] = carry + digits[i]
                return digits
            else:
                digits[i], carry = (carry + digits[i])%10, (carry + digits[i])//10
        if carry != 0:
            digits.insert(0, carry)
        return digits