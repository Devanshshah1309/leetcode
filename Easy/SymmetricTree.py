# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isSameTree(left: TreeNode | None, right: TreeNode | None):
            if left == None or right == None:
                return left == None and right == None
            return left.val == right.val and isSameTree(left.left, right.left) and isSameTree(left.right, right.right)
        def reverseTree(node: TreeNode | None):
            if node == None:
                return
            node.left, node.right = node.right, node.left
            reverseTree(node.left)
            reverseTree(node.right)
        if root == None:
            return True
        reverseTree(root.left)
        return isSameTree(root.left, root.right)
        

        