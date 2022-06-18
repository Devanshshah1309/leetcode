# O(n^2) time and O(1) space (expansion from the centre technique)
class Solution:
    def countSubstrings(self, s: str) -> int:
        # how many palindromes have l,r as their centre character(s)
        # for odd length palindrome, only one central character, i.e., l == r
        # for even length palindrome, two central characters, i.e., r = l + 1
        def helper(l: int, r: int):
            count = 0 # actually we can just use global count (save some space too haha)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        count = 0
        for i in range(len(s)):
            count += helper(i, i) # odd length palindromes
            count += helper(i, i+1) # even length palindrome
            
        return count
# This can also be solved using DP in O(n^2) time and O(n^2) time --> dp[i][j] == True if the substring from i to j is a palindrome.
# The recursive relation is as follows:
#   1. if len(substring) > 2:
#       it is a palindrome if the extreme 2 characters are equal and the rest of the middle characters form a palindrome, i.e., s[i] == s[j] && dp[i + 1][j - 1] is True (you need to consider for even, odd length palindromes here by making sure that i < j at every step)
