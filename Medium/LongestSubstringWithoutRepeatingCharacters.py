class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevMax = 0
        curr = 0
        currString = ""
        d = {} # key: character, value: index at which it occurs
        for i in range(len(s)):
            if s[i] not in d:
                curr += 1
                d[s[i]] = i
                currString += s[i]
            else:
                occurred = d[s[i]] # index at which this character occurred previously. Now, we need to remove this character and all chars preceeding it in the dictionary
                prevMax = max(prevMax, curr)
                for j in range(curr):
                    if currString[j] == s[i]:
                        d.pop(s[i])
                        break
                    d.pop(currString[j])
                currString += s[i]
                d[s[i]] = i
                currString = currString[j + 1:]
                curr = len(currString)
        # invariants: curr == len(currString); for all char in currString, char in d == true

        return max(prevMax, curr)

