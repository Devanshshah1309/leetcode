# O(n) time and O(1) space (where n = number of nodes in the binary tree)
# (since you are "visiting" each node exactly once)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
