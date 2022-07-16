# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)
        if n == 0:
            return None
        mid = n//2
        ans = TreeNode(nums[mid])
        ans.left = self.sortedArrayToBST(nums[:mid])
        ans.right = self.sortedArrayToBST(nums[mid+1:])
        return ans
        