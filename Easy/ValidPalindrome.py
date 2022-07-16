class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Note: string appending is O(n) since the entire string is copied over and a new string is created
        # So, it is always better to convert a string into a list and then join back to a string
        l = list(s)
        # filter out non-alphanumeric chars. convert remaining to lowercase
        ans = list(map(lambda char: char.lower(), list(filter(lambda char: char.isalnum() and not char.isspace(), l))))
        return ans == ans[::-1]