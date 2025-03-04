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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res 
            if not root:
                return 0
            print("root:", root.val)
            left = dfs(root.left)
            print("left:", left)
            right = dfs(root.right)
            print("right:", right)
            res = max(res, right + left)
            print("res:", res)
            return max(left, right) + 1

        dfs(root)
        return res

        # def heightNode(root):
        #     if not root:
        #         return 0
        #     else:
        #         return 1 + max(heightNode(root.left), heightNode(root.right))

        # def diameterNode(root):
        #     diameter = 0
        #     if not root:
        #         return 0
        #     left = heightNode(root.left)
        #     right = heightNode(root.right)
        #     diameter = left + right
        #     temp = max(diameterNode(root.left), diameterNode(root.right))
        #     return max(diameter, temp)

        # res = diameterNode(root)
        # return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().diameterOfBinaryTree(root))  # Output should be 3