# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:   
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.heightOfTree(root.left) 
        right = self.heightOfTree(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def heightOfTree(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().isBalanced(root))