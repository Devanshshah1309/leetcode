# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Observation: there are only as many root-to-leaf paths as there are leaves
        # This is true because each node (except the root) has exactly one parent
        # So, exploring all root-to-leaf paths takes O(n)
        # Note that this question does not require DP as there are no **overlapping** subproblems
        if root == None:
            return False
        if root.left == None and root.right == None: # leaf node
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

