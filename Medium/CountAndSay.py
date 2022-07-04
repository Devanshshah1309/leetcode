class Solution:
    def countAndSay(self, n: int) -> str:
        # i -> tracks current count and say iteration
        # s -> tracks current count and say sequence
        def countAndSayHelper(s: str, i: int) -> str:
            if i == n:
                return s
            else:
                currDigit = None
                currDigitCount = 0
                # list appending is O(1) whereas string appending is O(n) (which would have led to O(n^2)) --> neat trick whenever you want to convert n O(n) string concatenations into an O(n) operation :)
                nextString = []
                for char in s:
                    if char == currDigit:
                        currDigitCount += 1
                    else:
                        if currDigit != None: nextString.append(str(currDigitCount) + str(currDigit))
                        currDigit = char
                        currDigitCount = 1
                if currDigitCount != 0: 
                    nextString.append(str(currDigitCount) + str(currDigit))
                return countAndSayHelper(''.join(nextString), i + 1) # string join is an O(1) operation in this case noice
        return countAndSayHelper("1", 1)