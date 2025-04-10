# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, low=float("-inf"), high=float("inf")):
            if not root:
                return True
            if low >= root.val:
                return False
            if high <= root.val:
                return False
            return validate(root.left, low, root.val) and validate(
                root.right, root.val, high
            )

        return validate(root)
