# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Note: Just using node.val to store node.height since apparently you cannot add attributes to an object in Leetcode
        # Observation: A tree is height-balanced iff all its nodes are height-balanced (by definition)
        def getHeight(node: TreeNode | None): # only called when node.val has been assigned a value
            if node == None:
                return -1 # this works because of the fact that leaves have a height = 0
            return node.val
        def assignHeights(node: TreeNode | None):
            if node == None:
                return
            if node.left == None and node.right == None:
                node.val = 0
                return
            assignHeights(node.left)
            assignHeights(node.right)
            node.val = 1 + max(getHeight(node.left), getHeight(node.right))
        def checkHeights(node: TreeNode | None) -> bool:
            if node == None:
                return True
            return abs(getHeight(node.left)-getHeight(node.right)) <= 1 and checkHeights(node.left) and checkHeights(node.right)
        assignHeights(root)
        return checkHeights(root)
        